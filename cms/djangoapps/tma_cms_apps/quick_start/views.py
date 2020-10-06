import logging
log = logging.getLogger()

import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from edxmako.shortcuts import render_to_response
from lms.djangoapps.tma_apps.models import TmaCourseOverview
from openedx.core.djangoapps.site_configuration.models import SiteConfiguration
from datetime import datetime
from django.views.decorators.http import require_http_methods
from tma_cms_apps.quick_start.serializer import CourseSerializer
from cms.djangoapps.tma_cms_apps.programs.models import TmaProgramOverview, TmaProgramCourse
from cms.djangoapps.tma_cms_apps.programs.serializer import ProgramSerializer  
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from lms.djangoapps.courseware.courses import get_course_by_id
from opaque_keys.edx.keys import CourseKey
from tma_cms_apps.quick_start.helpers import TmaCourseManager, TmaCourseInfo
from datetime import datetime  
from dateutil.relativedelta import relativedelta
from django.conf import settings
from contentstore.views.course import get_courses_accessible_to_user, _process_courses_list
from openedx.core.djangoapps.lang_pref.api import released_languages
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from lms.djangoapps.tma_apps.zones.helper import ZoneManager
from lms.djangoapps.instructor.enrollment import enroll_email


@login_required
@ensure_csrf_cookie
def quick_start(request):
    context={}
    organizations_options = list(configuration_helpers.get_all_orgs())
    #TRANSLATIONS
    translations = json.load(open("/edx/app/edxapp/edx-platform/cms/djangoapps/tma_cms_apps/quick_start/quick_start_trads.json"))
    language = request.LANGUAGE_CODE
    if not language in translations:
        language="en"
    context["translations"]=translations[language]

    #CONFIG
    config = json.load(open("/edx/app/edxapp/edx-platform/cms/djangoapps/tma_cms_apps/quick_start/quick_start_config.json"))
    context.update(config)

    context["courseBasis"].update({
        "start_date":datetime.now(),
        "end_date":datetime.today() + relativedelta(months=+6)
    })

    context["programBasis"].update({
        "start_date":datetime.now(),
        "end_date":datetime.today() + relativedelta(months=+6)
    })

    #COURSES
    courses_iter, in_process_course_actions = get_courses_accessible_to_user(request, org=None)
    active_courses, archived_courses = _process_courses_list(courses_iter, in_process_course_actions, split_archived=False)
    

    coursesList = []
    for course in active_courses:
        tmaOverview = TmaCourseOverview.get_tma_course_overview_by_course_id(SlashSeparatedCourseKey.from_deprecated_string(course['course_key']))
        if tmaOverview and tmaOverview.course_overview_edx.org in organizations_options:
            coursesList.append(TmaCourseInfo(tmaOverview=tmaOverview).getShortInfo())

    context['lmsBase'] = str("https://"+settings.LMS_BASE)
    context['courses'] = coursesList
    
    #PROGRAMS
    programs_list = []
    

    for program in TmaProgramOverview.objects.all():
        
        course_overview = TmaProgramCourse.objects.get(program=program, order=0).course
        tma_course_overview = TmaCourseOverview.get_tma_course_overview_by_course_id(course_overview.id)
        email_url = TmaCourseInfo(tmaOverview=tma_course_overview).get_course_links()['email_url']
        statistics_url = TmaCourseInfo(tmaOverview=tma_course_overview).get_course_links()['statistics_url']

        program_dict = program.__dict__
        program_dict['email_url'] = email_url
        program_dict['statistics_url'] = statistics_url

        program_courses = []
        for program_course in TmaProgramCourse.objects.filter(program=program):
            course_name = str(program_course.course.display_name_with_default)
            course_id = program_course.course.id
            program_courses.append({'course_name':course_name, 'course_id':str(course_id)})

        program_dict['program_courses'] = json.dumps(program_courses)
        
        program_serializer = ProgramSerializer(program_dict)
        programs_list.append(program_serializer.data)
    
    context['programs'] = programs_list

    #LANGUAGES AND ZONE
    language_options = [language.code for language in released_languages()]
    context['fields'].append({
        "name":"language",
        "type":"select",
        "options": language_options
    })
    context["zone"]=ZoneManager(request.user).get_user_zone()

    #ORGANIZATIONS
    if "phileas" in organizations_options: 
        organizations_options.remove("phileas")
    checkedOrg=[]
    if request.user.is_superuser:
        checkedOrg=""
    elif ZoneManager(request.user).get_user_zone() :
        checkedOrg=ZoneManager(request.user).get_user_zone()
    

    context["homeFiltersDetail"].append({
        "name":"org",
        "options":organizations_options,
        "checked":checkedOrg,
        "type":"checkbox"        
    })
    return render_to_response('/tma_cms_apps/quick_start.html', {"props":context})


@login_required
@require_http_methods(["GET"])
@csrf_exempt
def quick_start_checkid_exists(request, course_key_string):
    try :
        course_key=SlashSeparatedCourseKey.from_deprecated_string(course_key_string)
        course=get_course_by_id(course_key)
        response={"details":"invalid_new_id"}
    except :
        response={"details":"valid_new_id"}          
    return JsonResponse(response)

@login_required
@require_http_methods(["GET"])
@csrf_exempt
def quick_start_get_course_info(request, course_key_string):
    response={}
    tmaOverview = TmaCourseOverview.get_tma_course_overview_by_course_id(CourseKey.from_string(course_key_string))
    if tmaOverview:
        response= TmaCourseInfo(tmaOverview=tmaOverview).getDetailedInfo()
    return JsonResponse(response)

@login_required
@require_http_methods(["POST"])
@csrf_exempt
def quick_start_create(request):
    data = request.POST.copy()
    if data['end_date'] == 'null':
        data['end_date'] = ''
    serializer = CourseSerializer(data=data)
    course_image = request.FILES.get('course_image') if request.FILES.get('course_image') else data['course_image']
    teacher_image = request.FILES.get('teacher_image') if request.FILES.get('teacher_image') else data['teacher_image']

    #COURSE DOWNLOADS
    download_files=None
    download_files_titles=None

    downloads_files_keys=[key for key in request.FILES.keys() if (key.find('course_downloads')>-1) ]
    if request.POST.get('download_files_titles') :
        download_files_titles=json.loads(request.POST.get('download_files_titles'))
    if downloads_files_keys and download_files_titles:
        download_files=[{
            "title":download_files_titles[index],
            "file":request.FILES.get(value)
            } for index,value in enumerate(downloads_files_keys)]
    if serializer.is_valid():
        tmaCourseCreator = TmaCourseManager(request,serializer.validated_data, course_image, teacher_image, download_files)
        response=tmaCourseCreator.createUpdateCourse()
        if response['status']=="error":
            status=400
        else :
            status=200
        enroll_email(course_id= CourseKey.from_string(response['course_id']), student_email=request.user.email, auto_enroll=False, email_students=False )
        return JsonResponse(response, status=status)
    else :
        return JsonResponse({"details":serializer.errors, "status":"error"}, status=400)


