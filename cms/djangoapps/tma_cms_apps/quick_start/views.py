import json
import logging
log = logging.getLogger()
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from edxmako.shortcuts import render_to_response
from lms.djangoapps.tma_apps.models import TmaCourseOverview
from openedx.core.djangoapps.site_configuration.models import SiteConfiguration
from django.conf import settings
from datetime import datetime
from django.conf import settings

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
    try:
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

            status=""
            if not course.course_overview_edx.start :
                status="self_paced"
            elif course.end < datetime.now() :
                status="closed"
            else :
                status="open"


            courseInfos={
                "type": 'vodeclic' if course.is_vodeclic else 'phileas',
                "course_organisation":course.course_overview_edx.org,
                "course_name":course.course_overview_edx.display_name,
                "course_id":str(course.course_overview_edx.id),
                "configure_url":"/course/"+course.course_overview_edx.id,
                "stats_url":lmsOrgBase+"/course/"+course_id,
                "preview_url": lmsOrgBase+"/courses/"+course_id+"/courseware",
                "tag":course.tag,
                "onBoarding":course.onboarding,
                "is_new":course.is_new,
                "has_menu":course.has_menu,
                "is_course_graded":course.is_course_graded,
                "settings":courseSettings,
                "status":status
            }
            coursesList.append(coursesInfos)
    except:
        pass
    context['courses']=coursesList

    return render_to_response('/tma_cms_apps/quick_start.html', {"props":context})
