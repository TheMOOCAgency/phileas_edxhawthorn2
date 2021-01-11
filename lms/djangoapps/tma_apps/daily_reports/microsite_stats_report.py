# -*- coding: utf-8 -*-
import sys
import csv
import os
import json
import logging
import importlib

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lms.envs.aws")
os.environ.setdefault("lms.envs.aws,SERVICE_VARIANT", "lms")
os.environ.setdefault("PATH", "/edx/app/edxapp/venvs/edxapp/bin:/edx/app/edxapp/edx-platform/bin:/edx/app/edxapp/.rbenv/bin:/edx/app/edxapp/.rbenv/shims:/edx/app/edxapp/.gem/bin:/edx/app/edxapp/edx-platform/node_modules/.bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin")

os.environ.setdefault("SERVICE_VARIANT", "lms")
os.chdir("/edx/app/edxapp/edx-platform")

startup = importlib.import_module("lms.startup")
startup.run()

from django.utils import timezone
from django.contrib.auth.models import User
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from lms.djangoapps.tma_apps.models import TmaCourseOverview, TmaCourseEnrollment
from cms.djangoapps.tma_cms_apps.programs.models import TmaProgramCourse
from student.models import UserProfile, CourseEnrollmentAllowed
from xlwt import *
import operator
from io import BytesIO
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
log = logging.getLogger()

data = {}
org = sys.argv[1]
emails = sys.argv[2].split(';')
today = timezone.now()
# likes_counter = 0
users_counter = 0
last_month_visitors_counter = 0
courses_ranking_list = []
users_per_country = {}
visitors_per_country_last_month = {}

# GET MICROSITE USERS AND CURRENT MONTH VISITORS COUNT
users = User.objects.all()

for user in users:
  user_profile, created = UserProfile.objects.get_or_create(user=user)
  custom_field = user_profile.custom_field
  
  try:
    # GET USERS COUNT PER COUNTRY
    user_org = json.loads(custom_field).get('microsite', None)
    if user_org == org:
      user_country = user_profile.country.name

      if user_country and user_country in users_per_country.keys():
        users_per_country[user_country] += 1
      elif user_country:
        users_per_country[user_country] = 1
        visitors_per_country_last_month[user_country] = 0

      users_counter +=1

      last_login_year = user.last_login.year
      last_login_month = user.last_login.month

      # HANDLE NEW YEAR CASE
      last_month = today.month - 1 if today.month > 1 else 12
      last_month_year = today.year if last_month != 12 else today.year - 1

      # GET LAST MONTH UNIQUE VISITORS PER COUNTRY
      if last_login_year == last_month_year and last_login_month == last_month:
        if user_country and user_country in visitors_per_country_last_month.keys():
          visitors_per_country_last_month[user_country] += 1
        last_month_visitors_counter += 1
  except:
    pass

sorted_countries = sorted(users_per_country.items(), key=operator.itemgetter(1),reverse=True)

data['users_count'] = users_counter
data['unique_visitors_count'] = last_month_visitors_counter
data['users_per_country'] = sorted_countries
data['visitors_per_country_last_month'] = visitors_per_country_last_month

# COUNT ONGOING PROGRAMS COUNT BY GETTING FIRST COURSE COUNT
data['programs_count'] = TmaProgramCourse.objects.filter(course__org=org, course__start__lte=today, course__end__gte=today, order=0).count()

# COUNT ONGOING COURSES COUNT
courses = TmaCourseOverview.objects.filter(course_overview_edx__org=org, course_overview_edx__start__lte=today, course_overview_edx__end__gte=today).exclude(course_overview_edx__id__icontains='duplicated')
data['courses_count'] = courses.count()

# GET TOP COURSES OF THE MONTH, IN TERMS OF ENROLLMENTS
for course in courses:
  # BELOW MUTED VARIABLE IS FOR TEST CASES
  current_month_enrollments = TmaCourseEnrollment.objects.filter(course_enrollment_edx__course=course.course_overview_edx)
  #current_month_enrollments = TmaCourseEnrollment.objects.filter(course_enrollment_edx__course=course.course_overview_edx, course_enrollment_edx__created__year=today.year, course_enrollment_edx__created__month=today.month)
  enrollments_count = current_month_enrollments.count()

  # ORDER COURSES LIST BY COURSE ENROLLMENTS COUNT
  if not courses_ranking_list:
    courses_ranking_list.append(current_month_enrollments)
  else:
    if enrollments_count >= courses_ranking_list[0].count():
      courses_ranking_list.insert(0, current_month_enrollments)
    elif enrollments_count <= courses_ranking_list[len(courses_ranking_list) -1].count():
      courses_ranking_list.append(current_month_enrollments)
    else:
      for index, course_enrollments in enumerate(courses_ranking_list):
        if enrollments_count > course_enrollments.count():
          courses_ranking_list.insert(index, current_month_enrollments)
          break

# GET MICROSITE LIKES COUNT
# all_org_courses = courses = TmaCourseOverview.objects.filter(course_overview_edx__org=org).exclude(course_overview_edx__id__icontains='duplicated')

# for course in all_org_courses:
#   likes_counter += course.liked_total

# data['likes_count'] = int(likes_counter)
data['courses_data'] = {}

# GET DATA FROM TOP 5 COURSES
for enrollments_list in courses_ranking_list:
  if enrollments_list:
    course_overview = enrollments_list[0].course_enrollment_edx.course
    course_id = course_overview.id
    all_course_enrollments = TmaCourseEnrollment.objects.filter(course_enrollment_edx__course=course_overview)
    course_enrollments_count = all_course_enrollments.count()
    validated_courses_counter = 0
    invited_users_counter = 0

    # CALCULATE COMPLETION RATE PER COURSE
    for enrollment in all_course_enrollments:
      if enrollment.has_validated_course:
        validated_courses_counter += 1

    course_completion_rate = int(float(validated_courses_counter) / course_enrollments_count * 100)
    invited_users_count = CourseEnrollmentAllowed.objects.filter(course_id=course_id).count()

    # DETERMINE IF COURSE IS OPEN OR CLOSED
    course_status = "open"
    if course_overview.enrollment_start and today < course_overview.enrollment_start:
      course_status = "closed"
    if course_overview.enrollment_end and today > course_overview.enrollment_end:
      course_status = "closed"\

    liked_total = TmaCourseOverview.objects.get(course_overview_edx=course_overview).liked_total

    data['courses_data'][str(course_id)] =  {
      'course_completion_rate': course_completion_rate,
      'course_enrollments_count': course_enrollments_count,
      'invited_users_count': invited_users_count,
      'likes_total': liked_total,
      'course_status': course_status
    }
  else:
    data['courses_data']['No enrollments yet'] =  {
      'course_completion_rate': 0,
      'course_enrollments_count': 0,
      'invited_users_count': 0,
      'likes_total': 0,
      'course_status': None
    }


# GENERATE XLS FILE
wb = Workbook(encoding='utf-8')
title = 'Data report - Phileas - {} - {}'.format(org, today.strftime("%m/%y"))
filename = 'Phileas_data-{}-{}.xls'.format(org, today.strftime("%m/%y"))

sheet = wb.add_sheet(org)
row = 0
col = 0
sheet.write(row,col, title)
row += 1

# RENDER HEADER
sheet.write(row, 1, 'Total number of users')
sheet.write(row, 2, 'Unique visitors this month')
sheet.write(row, 4, 'Open courses')
sheet.write(row, 5, 'Open programs')
sheet.write(row, 8, 'Open/Closed')
sheet.write(row, 9, 'Invitations (this month)')
sheet.write(row, 10, 'Enrollments (this month)')
sheet.write(row, 11, 'Completion rate (All times)')
sheet.write(row, 12, 'Likes (All times)')
row += 1

sheet.write(row, 0, 'Total')
sheet.write(row, 1, data['users_count'])
sheet.write(row, 2, data['unique_visitors_count'])
sheet.write(row, 4, data['courses_count'])
sheet.write(row, 5, data['programs_count'])
sheet.write(row, 7, 'Total')

row += 1

# RENDER COUNTRIES DATA
for country in data['users_per_country']:
  sheet.write(row, 0, country[0])
  sheet.write(row, 1, country[1])
  sheet.write(row, 2, data['visitors_per_country_last_month'][country[0]])
  row += 1

row = 3

# RENDER COURSES DATA

for key, value in data['courses_data'].items():
  sheet.write(row, 7, key)
  sheet.write(row , 8, data['courses_data'][key]['course_status'])
  sheet.write(row , 9, data['courses_data'][key]['invited_users_count'])
  sheet.write(row, 10, data['courses_data'][key]['course_enrollments_count'])
  sheet.write(row, 11, str(data['courses_data'][key]['course_completion_rate']) + "%")
  sheet.write(row, 12, data['courses_data'][key]['likes_total'])
  row += 1

# sheet.write(row, col, 'Likes')
# sheet.write(row + 1, col, data['likes_count'])

output = BytesIO()
wb.save(output)
_files_values = output.getvalue()


# GENERATE EMAIL
html = "<html><head></head><body><p>Bonjour,<br/><br/>Vous trouverez en PJ le fichier : {}<br/><br/>Bonne réception<br>The MOOC Agency<br></p></body></html>".format(title)
part2 = MIMEText(html, 'html', 'utf-8')

for i in range(len(emails)):
   fromaddr = "ne-pas-repondre@themoocagency.com"
   toaddr = emails[i]
   msg = MIMEMultipart()
   msg['From'] = fromaddr
   msg['To'] = toaddr
   msg['Subject'] = title
   attachment = _files_values
   part = MIMEBase('application', 'octet-stream')
   part.set_payload(attachment)
   encoders.encode_base64(part)
   part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(filename))
   msg.attach(part)
   server = smtplib.SMTP('mail3.themoocagency.com', 25)
   server.starttls()
   server.login('contact', 'waSwv6Eqer89')
   msg.attach(part2)
   text = msg.as_string()
   server.sendmail(fromaddr, toaddr, text)
   server.quit()
   print 'mail send to '+ emails[i]
