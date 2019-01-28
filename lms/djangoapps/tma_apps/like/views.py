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
def api_update_like(request, course_id):
    response={}
    course_key = CourseKey.from_string(course_id)
    status = request.POST['status'].lower() in ("yes", "true", "t", "1")
    new_status = TmaCourseEnrollment.update_social_attributes("is_liked",course_key, request.user, status)
    new_status['course_id']=course_id.replace(':','').replace('+','')
    return JsonResponse(new_status)
