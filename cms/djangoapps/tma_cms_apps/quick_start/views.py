import logging
log = logging.getLogger()

import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from edxmako.shortcuts import render_to_response
from lms.djangoapps.tma_apps.models import TmaCourseOverview
from openedx.core.djangoapps.site_configuration.models import SiteConfiguration
from django.conf import settings
from datetime import datetime
from django.conf import settings
from django.views.decorators.http import require_http_methods
from tma_cms_apps.quick_start.serializer import CourseSerializer 
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from lms.djangoapps.courseware.courses import get_course_by_id

@login_required
@ensure_csrf_cookie
def quick_start(request):
    context={}
    #TRANSLATIONS
    translations = json.load(open("/edx/app/edxapp/edx-platform/cms/djangoapps/tma_cms_apps/quick_start/quick_start_trads.json"))
    context["translations"]=translations['fr']

    #CONFIG
    config = json.load(open("/edx/app/edxapp/edx-platform/cms/djangoapps/tma_cms_apps/quick_start/quick_start_config.json"))
    context.update(config)

    #COURSES
    courses = TmaCourseOverview.objects.all()
    coursesList=[]
    courseInfos={}

    for course in courses :
        lmsOrgBase = SiteConfiguration.get_value_for_org(
            course.course_overview_edx.org,
            "LMS_BASE",
            settings.LMS_BASE
        )

        courseSettings=[]
        if course.is_mandatory:
            courseSettings.append('mandatory')
        if course.is_manager_only:
            courseSettings.append('manager_only')

        self_paced=True if course.course_overview_edx.self_paced else False
        course_id=str(course.course_overview_edx)

        courseInfos={
            "type": 'vodeclic' if course.is_vodeclic else 'phileas',
            "org":course.course_overview_edx.org,
            "course_name":course.course_overview_edx.display_name,
            "course_id": course_id,
            "configure_url":"/course/"+course_id,
            "stats_url":lmsOrgBase+"/course/"+course_id,
            "preview_url": lmsOrgBase+"/courses/"+course_id+"/courseware",
            "tag":course.tag,
            "onBoarding":course.onboarding,
            "is_new":course.is_new,
            "has_menu":course.has_menu,
            "is_course_graded":course.is_course_graded,
            "settings":courseSettings,
            "self_paced":self_paced
        }
        coursesList.append(courseInfos)

    context['courses']=coursesList
    return render_to_response('/tma_cms_apps/quick_start.html', {"props":context})


@csrf_exempt
def quick_start_create(request):
    data = json.loads(request.body)
    serializer = CourseSerializer(data=data)
    
    if serializer.is_valid():
        response=serializer.create(serializer.validated_data)
        if response['status']=="error":
            status=400
        else :
            status=200    
        return JsonResponse(response, status=status)
    else :
        return JsonResponse({"details":serializer.errors}, status=400)


