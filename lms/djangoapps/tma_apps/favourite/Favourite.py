from student.models import CourseEnrollment
from tma_apps.models import TmaCourseEnrollment
from django.utils.translation import ugettext as _

import logging
log = logging.getLogger()

class Favourite():
    def __init__(self,request):
        self.request = request

    def update_favourite(self, course_key):
        response={}
        status=request.POST.get('status','')
        if status is not None and isinstance(status,bool) :
            if TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=self.request.user, course_enrollment_edx__course_id=course_key).exists() :
                new_status = TmaCourseEnrollment.update_favourite(course_key,self.request.user,status)
            else :
                newEnrollment = CourseEnrollment.enroll()
                newEnrollment.update_enrollment(is_active=False)
                TmaCourseEnrollment.objects.get_or_create(course_enrollment_edx=newEnrollment).is_favourite=status
            response={
                'new_favourites_status':new_status
            }

        else :
            response={
                'error':_('Wrong parameters')
            }
        return response
