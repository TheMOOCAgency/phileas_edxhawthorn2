import logging
log = logging.getLogger()

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from django.apps import apps
TmaCourseEnrollment = apps.get_model('tma_apps','TmaCourseEnrollment')
from opaque_keys.edx.keys import CourseKey
from lms.djangoapps.grades.course_grade_factory import CourseGradeFactory
from courseware.courses import get_course_by_id
from django.utils.translation import ugettext as _
from lms.djangoapps.tma_apps.completion.completion import Completion


@login_required
@require_GET
def get_user_grade(request, course_id):
    course_key = CourseKey.from_string(course_id)
    course_descriptor = get_course_by_id(course_key)
    is_course_graded = not course_descriptor.no_grade

    response = {}
    response['is_course_graded'] = is_course_graded
    # Completion information
    completion_info = Completion(request).get_course_completion(course_id)

    # If course is graded
    if is_course_graded:
        user_grade_info = CourseGradeFactory().read(request.user, course_descriptor)
        update_status = TmaCourseEnrollment.update_grade(course_key, request.user, user_grade_info.percent, user_grade_info.passed)
        if update_status['status'] == "success":
            response.update(update_status)
            response['user_grade'] = user_grade_info.percent
            response['passed'] = user_grade_info.passed
            response.update(completion_info)
            # If user passed - has not already seen the popup - has completed all units
            if user_grade_info.passed and not response['has_displayed_message'] and completion_info['quiz_completion_rate'] == 1:
                response['has_completed'] = True
                response['graded_success'] = True
            # if user has failed
            elif not user_grade_info.passed and not response['has_displayed_message'] and completion_info['quiz_completion_rate'] == 1:
                response['has_completed'] = True
                response['graded_success'] = False
        else :
            response = {
                status:'error'
            }
    # If course is not graded
    elif not is_course_graded:
        response.update(completion_info)
        response['has_displayed_message'] = TmaCourseEnrollment.get_courseenrollment(course_key, request.user).has_displayed_message
        # Update date_best_student_grade
        date_update_status = TmaCourseEnrollment.update_not_graded_status(course_key, request.user, completion_info['completion_rate'])
        response.update(date_update_status)
        # If has not already seen the popup - has completed all units
        if not response['has_displayed_message'] and completion_info['completion_rate'] == 1:
            response['has_completed'] = True
            response['not_graded_success'] = True

    return JsonResponse(response)

@login_required
@require_POST
def mark_displayed_message(request, course_id):
    message_displayed_status = request.POST.get('message_displayed_status')
    try :
        enrollment = TmaCourseEnrollment.get_courseenrollment(CourseKey.from_string(course_id), request.user)
        enrollment.has_displayed_message = message_displayed_status
        enrollment.save()
        response = {'status':_('success registering status')}
    except :
        response = {'status':_('error while registering status')}
    return JsonResponse(response)


@login_required
@require_POST
def try_again(request, course_id):
    message_displayed_status = request.POST.get('message_displayed_status')
    try:
        enrollment = TmaCourseEnrollment.get_courseenrollment(CourseKey.from_string(course_id), request.user)
        enrollment.has_displayed_message = message_displayed_status
        enrollment.save()
        response = {'status':_('success resetting message status & score')}
    except :
        response = {'status':_('error while resetting message status & score')}
    return JsonResponse(response)