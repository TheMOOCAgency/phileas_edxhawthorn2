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
likes_counter = 0
users_counter = 0
visitors_counter = 0
top_courses_enrollments_list = []
countries_counter = {}

# GET MICROSITE USERS AND CURRENT MONTH VISITORS COUNT
users = User.objects.all()

for user in users:
  user_profile, created = UserProfile.objects.get_or_create(user=user)
  custom_field = user_profile.custom_field
  
  try:
    user_org = json.loads(custom_field).get('microsite', None)
    if user_org == org:
      user_country = user_profile.country.name

      if user_country and user_country in countries_counter.keys():
        countries_counter[user_country] += 1
      elif user_country:
        countries_counter[user_country] = 1

      last_login_year = user.last_login.year
      last_login_month = user.last_login.month
      users_counter +=1

      if last_login_year == today.year and last_login_month == today.month:
        visitors_counter += 1
  except:
    pass

sorted_countries = sorted(countries_counter.items(), key=operator.itemgetter(1),reverse=True)
sorted_countries = sorted_countries[0:5]

data['users_count'] = users_counter
data['unique_visitors_count'] = visitors_counter
data['top_countries'] = sorted_countries

# COUNT ONGOING PROGRAMS COUNT BY GETTING FIRST COURSE COUNT
data['programs_count'] = TmaProgramCourse.objects.filter(course__org=org, course__start__lte=today, course__end__gte=today, order=0).count()

# COUNT ONGOING COURSES COUNT
courses = TmaCourseOverview.objects.filter(course_overview_edx__org=org, course_overview_edx__start__lte=today, course_overview_edx__end__gte=today).exclude(course_overview_edx__id__icontains='duplicated')
data['courses_count'] = courses.count()

# GET TOP 5 COURSES OF THE MONTH, IN TERMS OF ENROLLMENTS
for course in courses:
  # BELOW MUTED VARIABLE IS FOR TEST CASES
  #current_month_enrollments = TmaCourseEnrollment.objects.filter(course_enrollment_edx__course=course.course_overview_edx)
  current_month_enrollments = TmaCourseEnrollment.objects.filter(course_enrollment_edx__course=course.course_overview_edx, course_enrollment_edx__created__year=today.year, course_enrollment_edx__created__month=today.month)
  enrollments_count = current_month_enrollments.count()

  # ORDER COURSES LIST BY COURSE ENROLLMENTS COUNT
  if not top_courses_enrollments_list:
    top_courses_enrollments_list.append(current_month_enrollments)
  else:
    if enrollments_count >= top_courses_enrollments_list[0].count():
      top_courses_enrollments_list.insert(0, current_month_enrollments)
    elif enrollments_count <= top_courses_enrollments_list[len(top_courses_enrollments_list) -1].count():
      top_courses_enrollments_list.append(current_month_enrollments)
    else:
      for index, course_enrollments in enumerate(top_courses_enrollments_list):
        if enrollments_count > course_enrollments.count():
          top_courses_enrollments_list.insert(index, current_month_enrollments)
          break

top_courses_enrollments_list = top_courses_enrollments_list[0:5]

# GET MICROSITE LIKES COUNT
all_org_courses = courses = TmaCourseOverview.objects.filter(course_overview_edx__org=org).exclude(course_overview_edx__id__icontains='duplicated')

for course in all_org_courses:
  likes_counter += course.liked_total

data['likes_count'] = int(likes_counter)
data['top_courses'] = {}

# GET DATA FROM TOP 5 COURSES
for enrollments_list in top_courses_enrollments_list:
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

    data['top_courses'][str(course_id)] =  {
      'course_completion_rate': course_completion_rate,
      'course_enrollments_count': course_enrollments_count,
      'invited_users_count': invited_users_count,
    }
  else:
    data['top_courses']['No enrollments yet'] =  {
      'course_completion_rate': 0,
      'course_enrollments_count': 0,
      'invited_users_count': 0,
    }


# GENERATE XLS FILE
wb = Workbook(encoding='utf-8')
title = 'Rapport de donnees - Phileas - {} - {}'.format(org, today.strftime("%d/%m/%y"))
filename = 'phileas-{}-{}.xls'.format(org, today.strftime("%d/%m/%y"))

sheet = wb.add_sheet(org)
row = 0
col = 0
sheet.write(row,col, title)
row += 1
sheet.write(row, 0, 'Users')
sheet.write(row + 1, 0, data['users_count'])
col += 1
sheet.write(row, col, 'Unique visitors')
sheet.write(row + 1, col, data['unique_visitors_count'])
col += 1
sheet.write(row, col, 'Likes')
sheet.write(row + 1, col, data['likes_count'])
col += 1
sheet.write(row, col, 'Open courses')
sheet.write(row + 1, col, data['courses_count'])
col += 1
sheet.write(row, col, 'Open programs')
sheet.write(row + 1, col, data['programs_count'])
col += 1

# TOP 5 COUNTRIES
rank = 1
for country in data['top_countries']:
  sheet.write(row, col, 'Country {}'.format(rank))
  sheet.write(row + 1, col, country[0])
  col += 1
  sheet.write(row, col, 'Country users')
  sheet.write(row + 1, col, country[1])
  col += 1
  rank += 1

# TOP 5 COURSES
rank = 1
for key, value in data['top_courses'].items():
  sheet.write(row, col, 'Course {}'.format(rank))
  sheet.write(row + 1, col, key)
  col += 1
  sheet.write(row, col, 'Invitations')
  sheet.write(row + 1, col, data['top_courses'][key]['invited_users_count'])
  col += 1
  sheet.write(row, col, 'Enrollments')
  sheet.write(row + 1, col, data['top_courses'][key]['course_enrollments_count'])
  col += 1
  sheet.write(row, col, 'Completion rate')
  sheet.write(row + 1, col, str(data['top_courses'][key]['course_completion_rate']) + "%")
  col += 1
  rank += 1

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
