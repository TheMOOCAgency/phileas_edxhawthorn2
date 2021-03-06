import json
import logging
log = logging.getLogger()

from django.db import IntegrityError, transaction
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
                # Update Course MetaData info
                response = {}
                new_course_metadata = {
                    'invitation_only': True if request.POST['invitation_only'] == "True" else False,
                    'no_grade': False if request.POST['is_graded'] == "True" else True,
                }

                try:
                    with transaction.atomic():
                        result = CourseMetadata.update_from_dict(
                            new_course_metadata,
                            course_module,
                            request.user
                        )
                        response['course_metadata'] = "Successfully updated"
                except IntegrityError:
                    response['course_metadata'] = "Error when updating"

                # Update TMA Course Overview
                new_tma_course_overview = {
                    'us_manager_only': True if request.POST['manager_only'] == "True" else False,
                    'is_mandatory': True if request.POST['is_mandatory']  == "True" else False,
                    'is_new': True if request.POST['is_new']  == "True" else False,
                    'has_menu': True if request.POST['has_menu']  == "True" else False,
                    'tag': str(request.POST['tag']),
                    'onboarding': str(request.POST['onboarding']),
                    'course_about': request.POST['course_about'],
                    'is_course_graded': True if request.POST['is_graded']  == "True" else False,
                }

                try: 
                    with transaction.atomic():
                        tma_course_overview = TmaCourseOverview.get_tma_course_overview_by_course_id(course_key)
                        for key, value in new_tma_course_overview.iteritems():
                            if 'tag' or 'onboarding' in key and value == '':
                                setattr(tma_course_overview, key, 'False')

                            setattr(tma_course_overview, key, value)
                            tma_course_overview.save()
                        response['tma_course_overview'] = "Successfully updated"
                except IntegrityError:
                    response['tma_course_overview'] = "Error when updating"

                return JsonResponse(response)
