import xlwt
import json
import datetime
from collections import OrderedDict

from opaque_keys.edx.keys import CourseKey
from student.models import User, UserProfile, ManualEnrollmentAudit, CourseEnrollmentAllowed, CourseEnrollment

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.http import HttpResponse

import logging

log = logging.getLogger()

@login_required
@require_GET
def download_invited_report(request, course_id):
    course_key = CourseKey.from_string(course_id)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="invited_learners.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # First row style
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # Headers 
    header_email = OrderedDict([('email', 'Email')])
    headers_user = OrderedDict([('first_name', 'First Name'), ('last_name', 'Last Name')])
    headers_profile = OrderedDict([('rpid', 'RPID'), ('iug', 'IUG')])
    header_customfield = OrderedDict([('zoneinfo', 'Zone Info'), ('societe.id', 'ID Society'), ('societe.name', 'Society Name'), ('societe.description', 'Society Description'), ('service', 'Service')])
    headers = list(header_email.values()) + list(headers_user.values()) + list(headers_profile.values()) + list(header_customfield.values()) + ['Invited']
    # Write headers in row[0]
    for i, header in enumerate(headers):
        ws.write(0, i, header, font_style)


    transition_states = ['from enrolled to enrolled', 'from unenrolled to enrolled']

    # Emails list of people invited by email but not yet registered on the platform when the email was sent
    invited_users_emails = CourseEnrollmentAllowed.objects.filter(course_id=course_key).values_list('email', flat=True)

    # Emails list of all people enrolled to course, except those we already know that they were invited by email
    enrolled_users = list(CourseEnrollment.objects.filter(course_id=course_key).exclude(user__email__in=invited_users_emails).values_list('user__email', flat=True))

    # Emails lists of people registered and not enrolled yet
    enrolled_to_enrolled = []
    # Emails lists of people registered and already enrolled
    unenrolled_to_enrolled = []

    for email in enrolled_users:
        manual_enrollments = ManualEnrollmentAudit.objects.filter(enrollment__course_id=course_key, enrolled_email=email, state_transition__in=transition_states)
        for me in manual_enrollments:
            # Those who were already enrolled when the invitation was sent
            if str(me.enrolled_email) not in enrolled_to_enrolled and me.state_transition == 'from enrolled to enrolled':
                enrolled_to_enrolled.append(str(me.enrolled_email))

        for me in manual_enrollments:
            # Those who were not already enrolled when the invitation was sent
            # It is possible that a n-th invitation was sent to a user who received a n-x invitation. If so, this user is already taken into account in the previous loop (user originally not enrolled then enrolled thanks to an invitation)
            if str(me.enrolled_email) not in unenrolled_to_enrolled and me.state_transition == 'from unenrolled to enrolled' and str(me.enrolled_email) not in enrolled_to_enrolled:
                unenrolled_to_enrolled.append(str(me.enrolled_email))

    j=0
    # Generate rows for non-existent users
    for invited_user in invited_users_emails:
        j+=1
        # Invited email
        student_email = str(invited_user)
        # N/A for all fields and "invited" flag
        student_user_fields = ["n/a" for field_name in headers_user] + ["n/a" for field_name in headers_profile] + ["n/a" for field_name in header_customfield]
        invited_or_enrolled = 'Invited'

        # Combine fields in one list
        fields = [student_email] + student_user_fields + [invited_or_enrolled]
    
        # Write fields in sheet
        for i, field in enumerate(fields):
            if isinstance(field, datetime.date):
                ws.write(j, i, field.strftime("%d-%m-%Y"))
            else:
                ws.write(j, i, field)

    # Generate rows for users already enrolled when the invitation was sent
    for enrolled_user in enrolled_to_enrolled:
        j+=1

        student_email = str(enrolled_user)
        student_user_fields = []

        for user in User.objects.filter(email=enrolled_user):
            student_user_fields = [getattr(user, field_name) if getattr(user, field_name) else "n/a" for field_name in headers_user]

        # Get profile info
        for profile in UserProfile.objects.filter(user__email=enrolled_user):
            student_user_fields = student_user_fields + [getattr(profile, field_name) if getattr(profile, field_name) else "n/a" for field_name in headers_profile]

            # Get custom field info 
            student_json_customfields = {} 
            try:      
                student_json_customfields = json.loads(profile.custom_field)
            except:
                pass
            student_user_fields = student_user_fields + [student_json_customfields[field_name] if field_name in student_json_customfields.keys() else "n/a" for field_name in header_customfield]

        invited_or_enrolled = 'Invited'

        fields = [student_email] + student_user_fields + [invited_or_enrolled]
    
        for i, field in enumerate(fields):
            if isinstance(field, datetime.date):
                ws.write(j, i, field.strftime("%d-%m-%Y"))
            else:
                ws.write(j, i, field)


    # Generate rows for users not already enrolled when the invitation was sent
    for enrolled_user in unenrolled_to_enrolled:
        j+=1

        student_email = str(enrolled_user)
        student_user_fields = []

        for user in User.objects.filter(email=enrolled_user):
            student_user_fields = [getattr(user, field_name) if getattr(user, field_name) else "n/a" for field_name in headers_user]

        for profile in UserProfile.objects.filter(user__email=enrolled_user):
            student_user_fields = student_user_fields + [getattr(profile, field_name) if getattr(profile, field_name) else "n/a" for field_name in headers_profile]

            student_json_customfields = {} 
            try:      
                student_json_customfields = json.loads(profile.custom_field)
            except:
                pass
            student_user_fields = student_user_fields + [student_json_customfields[field_name] if field_name in student_json_customfields.keys() else "n/a" for field_name in header_customfield]

        invited_or_enrolled = 'Invited'

        fields = [student_email] + student_user_fields + [invited_or_enrolled]
    
        for i, field in enumerate(fields):
            if isinstance(field, datetime.date):
                ws.write(j, i, field.strftime("%d-%m-%Y"))
            else:
                ws.write(j, i, field)

    wb.save(response)
    return response
