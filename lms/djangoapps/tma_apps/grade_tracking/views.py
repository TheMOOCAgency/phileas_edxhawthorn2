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


@login_required
@require_GET
def get_user_grade(request, course_id):
    course_key = CourseKey.from_string(course_id)
    user_grade_info = CourseGradeFactory().read(request.user, get_course_by_id(course_key))
    update_status = TmaCourseEnrollment.update_grade(course_key, request.user, user_grade_info.percent, user_grade_info.passed)
    if update_status['status']=="success":
        response={
            'status':'success',
            'user_grade':user_grade_info.percent,
            'passed':user_grade_info.passed,
            'new_best_grade':False
        }
        if update_status['new_best_grade'] :
            response['new_best_grade']=True
            popup_title=_('Congratulations!!!!')
            popup_text=_('You have finished your training.<br>To get your certificate click on the button.')
            response['popup_title']=popup_title
            response['popup_text']=popup_text
    else :
        response={
            status:'error'
        }
    return JsonResponse(response)
