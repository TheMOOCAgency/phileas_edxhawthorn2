import json
import logging
log = logging.getLogger()

from student.models import CourseEnrollment
from django.utils.translation import ugettext as _
from django.apps import tma_apps
TmaCourseEnrollment = tma_apps.get_model('TmaCourseEnrollment')

class Liked():
    def __init__(course_key, user):
        self.course_key=course_key
        self.user = user

    def get_liked_status(self):
        """
        Gets value of is_liked attribute from a given course
        """
        liked_status=False
        if TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=self.user, course_enrollment_edx__course_id=self.course_key).exists():
            liked_status = TmaCourseEnrollment.objects.get(course_enrollment_edx__user=self.user, course_enrollment_edx__course_id=self.course_key).is_liked
        return liked_status
