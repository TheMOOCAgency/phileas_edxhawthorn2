import xlwt
import datetime
from collections import OrderedDict

from opaque_keys.edx.keys import CourseKey
from student.models import User, UserProfile, ManualEnrollmentAudit

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
    headers = list(headers_allowed_user.values()) + list(headers_user.values()) + list(headers_profile.values()) + ['Invited/Enrolled']
    # Write headers in row[0]
    for i, header in enumerate(headers):
        ws.write(0, i, header, font_style)

    # Get list of invited users
    state_transitions = ['from unenrolled to allowed to enroll', 'from unenrolled to enrolled']
    invited_users = ManualEnrollmentAudit.objects.filter(state_transition__in=state_transitions)
    j=0
    # Generate rows
    for invited_user in invited_users:
        j+=1
        student_allowed_fields = []
        student_user_fields = []
        invited_or_enrolled = ''
        fields = []

        # Get email
        student_allowed_fields = [getattr(invited_user, field_name) if getattr(invited_user, field_name) else "n/a" for field_name in headers_allowed_user]

        # If user is not registered yet
        if invited_user.state_transition == 'from unenrolled to allowed to enroll':
            # N/A for all fields and "invited" flag
            student_user_fields = ["n/a" for field_name in headers_user] + ["n/a" for field_name in headers_profile]
            invited_or_enrolled = 'invited'
        else:
            # If user already exists and enrolled
            for user in User.objects.filter(email=invited_user.enrolled_email):
                student_user_fields = [getattr(user, field_name) if getattr(user, field_name) else "n/a" for field_name in headers_user]

            for profile in UserProfile.objects.filter(user__email=invited_user.enrolled_email):
                student_user_fields = student_user_fields + [getattr(profile, field_name) if getattr(profile, field_name) else "n/a" for field_name in headers_profile]

            invited_or_enrolled = 'enrolled'

        fields = student_allowed_fields + student_user_fields + [invited_or_enrolled]

        # Write fields in sheet
        for i, field in enumerate(fields):
            if isinstance(field, datetime.date):
                ws.write(j, i, field.strftime("%d-%m-%Y"))
            else:
                ws.write(j, i, field)

    wb.save(response)
    return response