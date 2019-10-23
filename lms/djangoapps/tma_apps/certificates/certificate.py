
from lms.djangoapps.grades.course_grade_factory import CourseGradeFactory
from courseware.courses import get_course_by_id
from edxmako.shortcuts import render_to_response
from django.utils.translation import ugettext as _
import logging

from datetime import date
from django.apps import apps
TmaCourseEnrollment = apps.get_model('tma_apps','TmaCourseEnrollment')
TmaCourseOverview = apps.get_model('tma_apps','TmaCourseOverview')

log = logging.getLogger()


class certificate():
    def __init__(self,user):
        self.user = user
        self.course = None
        self.course_grade = None
        self.completion_rate = None
        self.is_course_graded = False

    def get_certificate_status(self, course_key):
        passed = False
        self.is_course_graded = TmaCourseOverview.objects.get(course_overview_edx__id=course_key).is_course_graded

        if course_key is not None:
            self.course = get_course_by_id(course_key)
            if self.course is not None and self.user is not None:
                # If course is graded 
                if self.is_course_graded:
                    # Get best_student_grade
                    self.course_grade = TmaCourseEnrollment.objects.get(course_enrollment_edx__course_id=self.course.id, course_enrollment_edx__user_id=self.user.id).best_student_grade

                    # If this grade is zero, check CourseGradeFactory
                    if self.course_grade == 0.0:
                        self.course_grade = CourseGradeFactory().read(self.user, self.course)
                        passed = self.course_grade.passed
                    else:
                        # If best_student_grade passes
                        if self.course_grade >= self.course.grade_cutoffs['Pass']:
                            passed = True

                else:
                    # Check completion
                    self.completion_rate = TmaCourseEnrollment.objects.get(course_enrollment_edx__course_id=self.course.id, course_enrollment_edx__user_id=self.user.id).completion_rate
                    if self.completion_rate == 1:
                        passed = True
                
                TmaCourseEnrollment.update_course_validation(course_key, self.user, passed)

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
        certificate_info = TmaCourseEnrollment.get_courseenrollment(course_key, self.user)

        context = {
            "passed":passed,
            "course_name":self.course.display_name_with_default,
            "first_name":first_name,
            "last_name":last_name,
            "certificate_info":certificate_info
        }

        return render_to_response('tma_apps/certificate.html', context)


    def generate(self, course_key, score):
    	try:
            first_name = self.user.first_name
    	except:
    	    first_name = _("Unknown first name")
    	try:
            last_name = self.user.last_name
        except:
            last_name = _("Unknown last name")

        name = last_name+" "+first_name

        self.is_course_graded = TmaCourseOverview.objects.get(course_overview_edx__id=course_key).is_course_graded
        certificate_info = TmaCourseEnrollment.get_courseenrollment(course_key, self.user)

        if self.is_course_graded:
            # Override score and mark course as done
            grade = score/float(100)
            certificate_info.best_student_grade = grade
            certificate_info.date_best_student_grade = date.today()
        else:
            # Override completion
            certificate_info.completion_rate = 1
            certificate_info.date_best_student_grade = date.today()
        
        certificate_info.save()

        # Get new value of passed - should be true as best_grade is updated
        passed = self.get_certificate_status(course_key)

        context = {
            "passed": passed,
            "course_name":self.course.display_name_with_default,
            "first_name":first_name,
            "last_name":last_name,
            "certificate_info":certificate_info,
            "is_course_graded": self.is_course_graded
        }

        return render_to_response('tma_apps/certificate.html', context)