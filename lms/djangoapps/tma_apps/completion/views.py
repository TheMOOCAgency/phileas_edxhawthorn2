from .completion import Completion
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.http import JsonResponse
import logging

log = logging.getLogger()


@login_required
@require_GET
def get_course_completion(request,course_id):
    return JsonResponse(Completion(request).get_course_completion(course_id))
