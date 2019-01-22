from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from opaque_keys.edx.keys import CourseKey
from lms.djangoapps.tma_apps.models import TmaCourseEnrollment
import logging

log = logging.getLogger()


@login_required
@require_POST
def api_update_favourite(request, course_id):
    response={}
    course_key = CourseKey.from_string(course_id)
    status = request.POST['status'].lower() in ("yes", "true", "t", "1")
    new_status = TmaCourseEnrollment.update_social_attributes("is_favourite",course_key, request.user, status)
    response['status'] = new_status
    return JsonResponse(response)
