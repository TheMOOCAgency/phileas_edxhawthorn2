from lms.djangoapps.grades.course_grade_factory import CourseGradeFactory
from courseware.courses import get_course_by_id
from edxmako.shortcuts import render_to_response
from django.utils.translation import ugettext as _
import logging

from django.apps import apps
TmaCourseEnrollment = apps.get_model('tma_apps','TmaCourseEnrollment')

log = logging.getLogger()


class certificate():
    def __init__(self,user):
        self.user = user
        self.course = None
        self.courseGrade = None

    def get_certificate_status(self, course_key):
        passed=False
        if course_key is not None:
            self.course = get_course_by_id(course_key)
            if self.course is not None and self.user is not None:
                self.courseGrade = CourseGradeFactory().read(self.user, self.course)
                passed = self.courseGrade.passed
                TmaCourseEnrollment.update_course_validation(course_key,self.user, passed)
        return passed

    def check_course_certificate(self, course_key):
        certificate_status = self.get_certificate_status(course_key)
        response = {
            "has_certificate":certificate_status
        }
        return response

    def update_user_certificates(self):
        response={}
        response['certificates']={}
        enrollments = get_course_enrollments(self.user, None, [])
        for enrollment in enrollments :
            response['certificates'][str(enrollment.course_id)]=self.get_certificate_status(enrollment.course_id)
        return response


    def view(self, course_key):
        passed = self.get_certificate_status(course_key)
    	try:
            first_name = self.user.first_name
    	except:
    	    first_name = _("Unknown first name")
    	try:
            last_name = self.user.last_name
        except:
            last_name = _("Unknown last name")

        name = last_name+" "+first_name
        context = {
            "passed":passed,
            "course_name":self.course.display_name_with_default,
            "first_name":first_name,
            "last_name":last_name,
        }

        return render_to_response('tma_apps/certificate.html',context)
