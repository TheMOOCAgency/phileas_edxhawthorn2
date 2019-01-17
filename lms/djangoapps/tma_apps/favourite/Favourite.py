from student.models import CourseEnrollment
from django.utils.translation import ugettext as _

from django.apps import apps
TmaCourseEnrollment = apps.get_model('tma_apps','TmaCourseEnrollment')

import json
import logging
log = logging.getLogger()

class Favourite():
    def __init__(self,request):
        self.request = request

    def get_favourite_status(self, course_key):
        """
        Gets value of is_favorite attribute from a given course
        """
        response = {}
        if TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=self.request.user, course_enrollment_edx__course_id=course_key).exists():
            response['status'] = TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=self.request.user, course_enrollment_edx__course_id=course_key).is_favourite
        else:
            response['status'] = False
        return response


    def update_favourite(self, course_key):
        status = json.loads(self.request.POST.get('status',''))
        response = TmaCourseEnrollment.update_favourite(course_key, self.request.user, status)
        return response

