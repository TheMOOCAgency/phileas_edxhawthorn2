import json
import logging
log = logging.getLogger()

from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.utils.html import escape
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods, require_GET
from django.views.decorators.csrf import ensure_csrf_cookie
from util.json_request import JsonResponse, JsonResponseBadRequest, expect_json

from edxmako.shortcuts import render_to_response
from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey

from xmodule.modulestore.django import modulestore
from xmodule.tabs import InvalidTabsException
from models.settings.course_metadata import CourseMetadata
from contentstore.views.course import get_course_and_check_access, _refresh_course_tabs

from lms.djangoapps.tma_apps.models import TmaCourseOverview
from models.settings.course_metadata import CourseMetadata

@login_required
@ensure_csrf_cookie
@require_http_methods(("GET", "POST", "PUT"))
@expect_json
def amundi_settings_handler(request, course_key_string):
    """
    Course settings configuration
    GET
        html: get the page
    POST
        json: update the Course's settings. The payload is a json rep of the
            metadata dicts.
    """
    course_key = CourseKey.from_string(course_key_string)
    tma_course_overview = TmaCourseOverview.get_tma_course_overview_by_course_id(course_key)

    with modulestore().bulk_operations(course_key):
        course_module = get_course_and_check_access(course_key, request.user)
        if 'text/html' in request.META.get('HTTP_ACCEPT', '') and request.method == 'GET':
            return render_to_response('settings_amundi.html', {
                'context_course': course_module,
                'is_new':course_module.is_new,
                'invitation_only': course_module.invitation_only,
                'is_manager_only': tma_course_overview.is_manager_only,
                'is_graded': not CourseMetadata.fetch(course_module).get('no_grade')['value'],
                'is_mandatory': tma_course_overview.is_mandatory,
                'has_menu': tma_course_overview.has_menu,
                'course_tag': tma_course_overview.tag,
                'onboarding_tag': tma_course_overview.onboarding,
                'course_about': tma_course_overview.course_about
            })
        elif 'application/json' in request.META.get('HTTP_ACCEPT', ''):
            if request.method == 'GET':
                return JsonResponse(CourseMetadata.fetch(course_module))
            else:
                #try:
                new_data = {
                    'is_new': request.POST['is_new'],
                    'invitation_only': request.POST['invitation_only'],
                    'no_grade': request.POST['is_graded'],
                }
                log.info(new_data)
                result = CourseMetadata.update_from_dict(
                    new_data,
                    course_module,
                    request.user
                )

                return JsonResponse(result)


def customize_settings(request,course_key_string):

    course_key = SlashSeparatedCourseKey.from_deprecated_string(course_key_string)
    with modulestore().bulk_operations(course_key):
        course_module = get_course_and_check_access(course_key, request.user)
        additional_info = {
        'is_new': request.POST.get('is_new', False),
        'invitation_only': request.POST.get('invitation_only', False),
        'manager_only': request.POST.get('manager_only', False),
        'grade_badge': request.POST.get('grade_badge', 100)
        }
        CourseMetadata.update_from_dict(additional_info, course_module, request.user)
        return JsonResponse({'data':'data'})
