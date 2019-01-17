import Favourite
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from opaque_keys.edx.keys import CourseKey
import logging

log = logging.getLogger()


@login_required
@require_POST
def update_favourite(request, course_id):
    course_key = CourseKey.from_string(course_id)
    return JsonResponse(Favourite.Favourite(request).update_favourite(course_key))

@login_required
@require_GET
def get_favourite(request, course_id):
    course_key = CourseKey.from_string(course_id)
    return JsonResponse(Favourite.Favourite(request).get_favourite_status(course_key))
