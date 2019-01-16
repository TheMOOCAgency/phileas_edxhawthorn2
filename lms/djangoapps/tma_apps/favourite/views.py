import Favourite
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from opaque_keys.edx.keys import CourseKey
import logging

log = logging.getLogger()


@login_required
@require_POST
def update_favourite(request,course_id):
    course_key = CourseKey.from_string(course_id)
    return JsonResponse(Favourite(request).update_favourite(course_key))
