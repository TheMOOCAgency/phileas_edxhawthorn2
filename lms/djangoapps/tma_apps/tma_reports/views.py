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

    # Sheet header, first row
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # Headers 
    headers_allowed_user = OrderedDict([('enrolled_email', 'Email'), ('time_stamp', 'Email sent')])
    headers_user = OrderedDict([('first_name', 'First Name'), ('last_name', 'Last Name')])
    headers_profile = OrderedDict([('rpid', 'RPID'), ('iug', 'IUG')])
    header_customfield = OrderedDict([('zoneinfo', 'Zone Info'), ('societe.id', 'ID Society'), ('societe.name', 'Society Name'), ('societe.description', 'Society Description'), ('service', 'Service')])
    headers = list(headers_allowed_user.values()) + list(headers_user.values()) + list(headers_profile.values()) + list(header_customfield.values()) + ['Invited/Started']
    # Write headers in row[0]
    for i, header in enumerate(headers):
        ws.write(0, i, header, font_style)

    # Get list of invited users
    state_transitions = ['from unenrolled to allowed to enroll', 'from unenrolled to enrolled']
    invited_users = ManualEnrollmentAudit.objects.filter(state_transition__in=state_transitions)
    j=0
    # Generate rows
    for invited_user in invited_users:

        # Check only users related to this course_id, whether they exists or not:
        if CourseEnrollmentAllowed.objects.filter(email=invited_user.enrolled_email, course_id=course_key).exists() or CourseEnrollment.objects.filter(user__email=invited_user.enrolled_email, course_id=course_key).exists() and (invited_user.state_transition in state_transitions):

            log.info(invited_user.enrolled_email)

            j+=1
            student_allowed_fields = []
            student_user_fields = []
            student_customfields = []
            invited_or_enrolled = ''
            fields = []

            # If user is not registered yet and was invited to this course
            if invited_user.state_transition == 'from unenrolled to allowed to enroll':
                # Get email
                student_allowed_fields = [getattr(invited_user, field_name) if getattr(invited_user, field_name) else "n/a" for field_name in headers_allowed_user]

                # N/A for all fields and "invited" flag
                student_user_fields = ["n/a" for field_name in headers_user] + ["n/a" for field_name in headers_profile] + ["n/a" for field_name in header_customfield]
                invited_or_enrolled = 'invited'

            # If user registered
            if invited_user.state_transition == 'from allowed to enroll to enrolled':
                # Get email
                student_allowed_fields = [getattr(invited_user, field_name) if getattr(invited_user, field_name) else "n/a" for field_name in headers_allowed_user]

                # If user already exists and enrolled : get user info
                for user in User.objects.filter(email=invited_user.enrolled_email):
                    student_user_fields = [getattr(user, field_name) if getattr(user, field_name) else "n/a" for field_name in headers_user]

                # Get profile info
                for profile in UserProfile.objects.filter(user__email=invited_user.enrolled_email):
                    student_user_fields = student_user_fields + [getattr(profile, field_name) if getattr(profile, field_name) else "n/a" for field_name in headers_profile]

                    # Get custom field info 
                    student_json_customfields = {} 
                    try:      
                        student_json_customfields = json.loads(profile.custom_field)
                    except:
                        pass
                    student_customfields = [student_json_customfields[field_name] if field_name in student_json_customfields.keys() else "n/a" for field_name in header_customfield]

                invited_or_enrolled = 'started'

            # Combine fields in one list
            fields = student_allowed_fields + student_user_fields + student_customfields + [invited_or_enrolled]
        
            # Write fields in sheet
            for i, field in enumerate(fields):
                if isinstance(field, datetime.date):
                    ws.write(j, i, field.strftime("%d-%m-%Y"))
                else:
                    ws.write(j, i, field)

    wb.save(response)
    return response