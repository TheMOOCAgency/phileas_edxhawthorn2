from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_GET,require_http_methods
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from student.models import User, UserProfile, CourseEnrollment
from lms.djangoapps.grades.course_grade_factory import CourseGradeFactory

from edxmako.shortcuts import render_to_response
from opaque_keys.edx.keys import CourseKey

from lms.djangoapps.courseware.courses import (
  get_course_overview_with_access,
)

from student.views.dashboard import _student_dashboard
from cms.djangoapps.tma_cms_apps.programs.models import TmaProgramOverview, TmaProgramCourse

import logging
log = logging.getLogger(__name__)

@login_required
def home_dashboard_courses(request):
    context = _student_dashboard(request)
    return render_to_response('tma_apps/home_dashboard.html', context)

@login_required
@ensure_csrf_cookie
def programs_dashboard_view(request):
    context = {}
    all_programs = {}
    all_courses = {}

    for program in TmaProgramOverview.objects.all():

      all_programs[program.id] = program
      
      courses_list = []
      program_courses = TmaProgramCourse.objects.filter(program=program)
      
      for program_course in program_courses:
        courses_list.append(program_course.course.id)

      all_courses[program.id] = courses_list

    context['programs'] = all_programs
    context['courses'] = all_courses

    response = render_to_response('tma_apps/programs_dashboard.html', context)
    return response