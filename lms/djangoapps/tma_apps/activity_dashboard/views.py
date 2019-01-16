from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_GET,require_http_methods
from django.http import HttpResponse

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from student.models import User, UserProfile, CourseEnrollment
from lms.djangoapps.grades.course_grade_factory import CourseGradeFactory

from edxmako.shortcuts import render_to_response
from opaque_keys.edx.keys import CourseKey

from lms.djangoapps.courseware.courses import (
  get_course_overview_with_access,
)

import logging
log = logging.getLogger(__name__)


@login_required
def home_dashboard(request):
    user = request.user
    username = user.username

    context = {
        'username': username
    }

    return render_to_response('tma_apps/home_dashboard.html', context)