import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse

from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from student.views.dashboard import get_tma_course_info, get_tma_course_json, is_course_blocked, get_course_enrollments

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from shoppingcart.models import CourseRegistrationCode

import logging

log = logging.getLogger()

def get_tma_course_list(request):
    # Get organization
    current_organisation = configuration_helpers.get_value('course_org_filter','phileas')
    # Get course_overviews
    courses_to_display = CourseOverview.objects.filter(org=current_organisation)
    # Get course_enrollments for request user
    course_enrollments = get_course_enrollments(request.user, org_whitelist=None, org_blacklist=None)
    # Get blocked courses
    block_courses = frozenset(
        enrollment.course_id for enrollment in course_enrollments
        if is_course_blocked(
            request,
            CourseRegistrationCode.objects.filter(
                course_id=enrollment.course_id,
                registrationcoderedemption__redeemed_by=request.user
            ),
            enrollment.course_id
        )
    )

    tma_course_list = []
    for course in courses_to_display :
        course_info = get_tma_course_json(request.user, course.id, block_courses)
        tma_course_list.append(course_info)

    return tma_course_list
    
@login_required
@require_POST
def search_courses(request):
    course_list = get_tma_course_list(request)
    search_results = {}    

    query = request.POST.get('query') + ' success'

    return JsonResponse(course_list, safe=False)