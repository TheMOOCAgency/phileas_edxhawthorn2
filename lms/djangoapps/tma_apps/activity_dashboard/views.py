from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from edxmako.shortcuts import render_to_response
from student.views.dashboard import _student_dashboard, get_org_black_and_whitelist_for_site, get_course_enrollments
from student.models import CourseEnrollment
from cms.djangoapps.tma_cms_apps.programs.models import TmaProgramOverview, TmaProgramCourse
from lms.djangoapps.tma_apps.models import TmaCourseEnrollment
from lms.djangoapps.tma_apps.completion.completion import Completion
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
    program_enrollments = {}
    site_org_whitelist, site_org_blacklist = get_org_black_and_whitelist_for_site()
    course_enrollments = list(get_course_enrollments(request.user, site_org_whitelist, site_org_blacklist))
    
    if course_enrollments:
        for program in TmaProgramOverview.objects.all():
            # Check if user is enrolled to the first course of each program, to get program enrollment status
            first_program_course = TmaProgramCourse.objects.get(program=program, order=0)
            for enrollment in course_enrollments:
                if enrollment._course_id == first_program_course.course.id:  
                    program_courses = TmaProgramCourse.objects.filter(program=program)

                    # calculate average program completion rate based on individual courses rates
                    total_rates = 0
                    for program_course in program_courses:
                        course_enrollment_edx = CourseEnrollment.objects.get(user=request.user, course=program_course.course)
                        log.info(type(CourseEnrollment.objects.get(user=request.user, course=program_course.course)))
                        total_rates += int(TmaCourseEnrollment.objects.get(course_enrollment_edx=course_enrollment_edx).completion_rate * 100)
                    completion_rate = total_rates / len(list(program_courses))
                    
                    program_enrollments[program.id] = {}
                    program_enrollments[program.id]['program_overview'] = program.__dict__
                    program_enrollments[program.id]['courses_overview'] = list(program_courses)
                    program_enrollments[program.id]['completion_rate'] = completion_rate


    context['programs_enrollments'] = program_enrollments

    return render_to_response('tma_apps/programs_dashboard.html', context)
