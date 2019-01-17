from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from opaque_keys.edx.keys import CourseKey
from django.apps import apps
TmaCourseEnrollment = apps.get_model('tma_apps','TmaCourseEnrollment')
import logging

log = logging.getLogger()


@login_required
@require_POST
def api_update_liked(request, course_id):
    course_key = CourseKey.from_string(course_id)
    new_status = TmaCourseEnrollment.update_social_attributes('is_liked', self.course_key, self.user, status)
    response['status'] = new_status
    return JsonResponse(response)
