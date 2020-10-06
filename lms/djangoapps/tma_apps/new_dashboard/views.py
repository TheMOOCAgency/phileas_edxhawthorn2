from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from edxmako.shortcuts import render_to_response
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from student.models import CourseEnrollment
from django.contrib.auth.models import User
from django.http import JsonResponse

import logging
log = logging.getLogger()


@require_http_methods(["GET"])
def view_enrollments(request):
    user_enrollments_profiles = {}
    org_courses = {}
    org = configuration_helpers.get_value('course_org_filter', '')
    courses_overviews = CourseOverview.objects.filter(org=org)

    for course_overview in courses_overviews:
        # CREATE ORG COURSES DICT
        overview_dict = course_overview.__dict__
        org_courses[str(overview_dict['id'])] = {}
        org_courses[str(overview_dict['id'])] = {
            'start': overview_dict['start'],
            'end': overview_dict['end'],
            'enrollment_start': overview_dict['enrollment_start'],
            'enrollment_end': overview_dict['enrollment_end'],
            'display_name': overview_dict['display_name']   
        }


        # CREATE USER ENROLLMENTS AND PROFILE DETAILS DICT
        course_enrollments = CourseEnrollment.objects.filter(course=course_overview)
        for course_enrollment in course_enrollments:
            user_id = course_enrollment.user_id
            course_id = course_enrollment.course_id
            course_key_string = str(course_id)
            if user_id not in user_enrollments_profiles.keys():
                user = User.objects.get(id=user_id).__dict__
                user_enrollments_profiles[user_id] = {}
                user_enrollments_profiles[user_id] = {
                    'username': user['username'],
                    'id': user['id'],
                    'last_name': user['last_name'],
                    'first_name': user['first_name'],
                    'is_active': user['is_active'],
                    'email': user['email']
                }

                user_enrollments_profiles[user_id]['enrollments'] = {}

            if user_enrollments_profiles[user_id] and course_id not in user_enrollments_profiles[user_id]['enrollments'].keys():
                enrollment = course_enrollment.__dict__
                course = CourseOverview.objects.get(id=course_id).__dict__

                user_enrollments_profiles[user_id]['enrollments'][course_key_string] = {
                    'id': str(course['id']),
                    'start_date': course['start'],
                    'end_date': course['end'],
                    'enrollment_date': enrollment['created'],
                    'name': course['display_name']
                }

        response = {
            'user_enrollments_profiles': user_enrollments_profiles,
            'org_courses': org_courses
        }

    return JsonResponse(response)

@login_required
def new_tma_dashboard_view(request):
    context = {}

    primary_color = configuration_helpers.get_value('primary_color', 'black')
    secondary_color = configuration_helpers.get_value('secondary_color', 'grey')

    colors = {
        'primary_color': primary_color,
        'secondary_color': secondary_color
    }

    context['colors'] = colors
    log.info(context)

    return render_to_response('tma_apps/new_tma_dashboard.html', {"props":context})