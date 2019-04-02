import logging
log = logging.getLogger()

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from django.apps import apps
TmaCourseEnrollment = apps.get_model('tma_apps','TmaCourseEnrollment')
from student.models import User
from opaque_keys.edx.keys import CourseKey
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from lms.djangoapps.grades.course_grade_factory import CourseGradeFactory
from lms.djangoapps.instructor.enrollment import reset_student_attempts
from lms.djangoapps.instructor.views.tools import get_student_from_identifier, strip_if_string
from xmodule.modulestore.django import modulestore
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
    response['required_score'] = course_descriptor.grade_cutoffs['Pass']
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
        # If has not already seen the popup - has completed all units
        if not response['has_displayed_message'] and completion_info['completion_rate'] == 1:
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
def mark_as_done(request, course_id):
    course_key = CourseKey.from_string(course_id)
    course_descriptor = get_course_by_id(course_key)
    response = {}

    # Completion information if course is not Vodeclic
    if not request.POST.get('is_vodeclic'):
        completion_info = Completion(request).get_course_completion(course_id)
        # Update date_best_student_grade
        date_update_status = TmaCourseEnrollment.update_not_graded_status(course_key, request.user, completion_info['completion_rate'])
        response.update(date_update_status)
    # Completion 100% if course is Vodeclic
    else:
        completion_rate = 1
        date_update_status = TmaCourseEnrollment.update_not_graded_status(course_key, request.user, completion_rate)
        response.update(date_update_status)
    
    # Update has_validated
    try:
        marked_as_done = request.POST.get('marked_as_done')
        has_validated_status = TmaCourseEnrollment.update_course_validation(course_key, request.user, marked_as_done)
        response.update({'has_validated_status': has_validated_status})
    except:
        response.update({'status': 'error'})

    return JsonResponse(response)

@login_required
@require_POST
def try_again(request, course_id):
    user_moi = User.objects.get(email='staff@example.com')
    course_key = CourseKey.from_string(course_id)
    course = modulestore().get_course(course_key, depth=4)
    course_id_str = str(course_id)

    try:
        # RESET SCORE FOR ALL PROBLEMS IN COURSE
        for section in course.get_children():
            for subsection in section.get_children():
                for unit in subsection.get_children():
                    # For each unit which is not of html type
                    for problem in unit.get_children():
                        if problem.location.block_type != 'html':
                            problem_location = str(problem.location)
                            print(problem.location.block_type)
                            course_id = SlashSeparatedCourseKey.from_deprecated_string(course_id_str)
                            problem_to_reset = strip_if_string(problem_location)
                            student_identifier = request.user.email
                            student = None

                            if student_identifier is not None:
                                try:
                                    student = get_student_from_identifier(student_identifier)
                                except:
                                    print(student)
                            all_students = False
                            delete_module = True

                            try:
                                module_state_key = course_id.make_usage_key_from_deprecated_string(problem_to_reset)
                            except InvalidKeyError:
                                log.info('invalid Key'+ str(module_state_key))
                            if student:
                                try:
                                    reset_student_attempts(
                                        course_id,
                                        student,
                                        module_state_key,
                                        requesting_user=user_moi,
                                        delete_module=delete_module
                                    )
                                    response = {'status':_('success resetting message status & score')}
                                except:
                                    response = {'status':_('error while resetting message status & score')}
    except:
        response = {'status':_('An error occurred')}
    
    return JsonResponse(response)