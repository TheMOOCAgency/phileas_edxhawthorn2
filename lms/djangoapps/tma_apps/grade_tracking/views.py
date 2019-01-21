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
    user_grade_info = CourseGradeFactory().read(request.user, get_course_by_id(course_key))
    completion_info = Completion(request).get_course_completion(course_id)
    update_status = TmaCourseEnrollment.update_grade(course_key, request.user, user_grade_info.percent, user_grade_info.passed)

    response={}
    if update_status['status']=="success":
        response.update(update_status)
        response['user_grade']=user_grade_info.percent
        response['passed']=user_grade_info.passed
        response.update(completion_info)
        if user_grade_info.passed and not response['has_displayed_message'] and completion_info['quiz_completion_rate']==1:
            response['popup_title']=_('Congratulations!!!!')
            response['popup_text']=_('You have finished your training.<br>To get your certificate click on the button.')
    else :
        response={
            status:'error'
        }
    return JsonResponse(response)

@login_required
@require_POST
def mark_displayed_message(request, course_id):
    message_displayed_status = request.POST.get('message_displayed_status')
    try :
        enrollment = TmaCourseEnrollment.get_courseenrollment(CourseKey.from_string(course_id), request.user)
        enrollment.has_displayed_message=message_displayed_status
        enrollment.save()
        response={'status':_('success registering status')}
    except :
        response={'status':_('error while registering status')}
    return JsonResponse(response)
