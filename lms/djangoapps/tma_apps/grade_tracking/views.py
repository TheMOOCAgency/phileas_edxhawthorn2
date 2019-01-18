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




@login_required
@require_GET
def get_user_grade(request, course_id):
    course_key = CourseKey.from_string(course_id)
    user_grade = CourseGradeFactory().read(request.user, get_course_by_id(course_key))
    update_status = TmaCourseEnrollment.update_grade(course_key, request.user, user_grade.percent, user_grade.passed)
    return JsonResponse(update_status)
