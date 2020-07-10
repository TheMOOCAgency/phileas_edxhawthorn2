from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_GET,require_http_methods
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from openedx.core.djangoapps.util.maintenance_banner import add_maintenance_banner
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from student.models import User, UserProfile, CourseEnrollment
from lms.djangoapps.grades.course_grade_factory import CourseGradeFactory

from edxmako.shortcuts import render_to_response
from opaque_keys.edx.keys import CourseKey

from lms.djangoapps.courseware.courses import (
  get_course_overview_with_access,
)

from student.views.dashboard import _student_dashboard

import logging
log = logging.getLogger(__name__)

@login_required
def home_dashboard_courses(request):
    context = _student_dashboard(request)
    return render_to_response('tma_apps/home_dashboard.html', context)

@login_required
@ensure_csrf_cookie
@add_maintenance_banner
def programs_dashboard_view(request):
    # Temporary renders course dashboard context
    context = _student_dashboard(request)
    response = render_to_response('tma_apps/programs_dashboard.html', context)
    return response