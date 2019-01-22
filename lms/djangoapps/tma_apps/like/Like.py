import json
import logging
log = logging.getLogger()

from student.models import CourseEnrollment
from django.utils.translation import ugettext as _
from lms.djangoapps.tma_apps.models import TmaCourseEnrollment

class Like():
    def __init__(course_key, user):
        self.course_key=course_key
        self.user = user

    def get_like_status(self):
        """
        Gets value of is_favorite attribute from a given course
        """
        like_status=False
        if TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=self.user, course_enrollment_edx__course_id=self.course_key).exists():
            like_status = TmaCourseEnrollment.objects.get(course_enrollment_edx__user=self.user, course_enrollment_edx__course_id=self.course_key).is_liked
        return like_status
