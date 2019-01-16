from .certificate import certificate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from opaque_keys.edx.keys import CourseKey
from django.http import JsonResponse
import logging

log = logging.getLogger()


@login_required
@require_GET
def ensure(request,course_id):
    course_key = CourseKey.from_string(course_id)
    return JsonResponse(certificate(request.user).check_course_certificate(course_key))

@login_required
@require_GET
def render(request,course_id):
    course_key = CourseKey.from_string(course_id)
    return certificate(request.user).view(course_key)
