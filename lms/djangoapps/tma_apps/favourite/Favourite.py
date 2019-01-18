import json
import logging
log = logging.getLogger()

from student.models import CourseEnrollment
from django.utils.translation import ugettext as _
from lms.djangoapps.tma_apps.models import TmaCourseEnrollment

class Favourite():
    def __init__(course_key, user):
        self.course_key=course_key
        self.user = user

    def get_favourite_status(self):
        """
        Gets value of is_favorite attribute from a given course
        """
        favourite_status=False
        if TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=self.user, course_enrollment_edx__course_id=self.course_key).exists():
            favourite_status = TmaCourseEnrollment.objects.get(course_enrollment_edx__user=self.user, course_enrollment_edx__course_id=self.course_key).is_favourite
        return favourite_status
