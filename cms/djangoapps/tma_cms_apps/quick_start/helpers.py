import logging
log = logging.getLogger()

import json

from contentstore.views.course import create_new_course
from util.organizations_helpers import (
    add_organization_course,
    get_organization_by_short_name,
    organizations_enabled,
)
from openedx.core.djangoapps.models.course_details import CourseDetails
from xmodule.course_module import CourseFields
from django.contrib.auth.models import User
from lms.djangoapps.tma_apps.models import TmaCourseOverview
from django.core.urlresolvers import reverse
from models.settings.course_grading import CourseGradingModel
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from cms.djangoapps.contentstore.views.assets import update_course_run_asset


class TmaCourseCreator():
    def __init__(self, request):
        #self.creator = self._get_course_creator()
        self.creator = request.user

    def _get_course_creator(self):
        try:
            creator_user = User.objects.get(username='coursecreator')
        except User.DoesNotExist:
            creator_user = User.objects.create(
                username='coursecreator',
                email='coursecreator@tma.com',
                first_name='coursecreator',
                last_name='coursecreator',
                is_active=True,
                is_staff=True
            )
            creator_user.set_password('coursecreator')
            creator_user.save()
        return creator_user

    def _convert_seconds_to_time(self, seconds):
        minutes = int(seconds) // 60
        hours = minutes // 60
        rest_minutes = minutes % 60
        return str(hours)+":"+str(rest_minutes)


    def createCourse(self, data, course_image, teacher_image):
        try:
            #CREATE COURSE
            fields= {
            "display_name": data.get('course_name'),
            "start": data.get('start_date', CourseFields.start.default),
            "enrollment_start": data.get('start_date', CourseFields.start.default),
            }
            new_course = create_new_course(user=self.creator, org=data.get('org'), number=data.get('course_number'), run=data.get('course_session'),fields=fields)
            new_course_key=SlashSeparatedCourseKey.from_deprecated_string(str(new_course.id))

            course_image_upload=None
            if course_image:
                course_image_upload = update_course_run_asset(new_course_key, course_image)

            teacher_image_upload=None
            if teacher_image:
                teacher_image_upload = update_course_run_asset(new_course_key, teacher_image)


            #COURSE OVERVIEW
            additional_info = {
            'display_name': data.get('course_name'),
            'language': data.get('language'),
            'short_description': data.get('short_description'),
            'start_date':data.get('start_date', CourseFields.start.default),
            'end_date': data.get('end_date', CourseFields.end.default),
            'enrollment_start': data.get('start_date', CourseFields.start.default),
            'enrollment_end': data.get('end_date', CourseFields.end.default),
            'effort':self._convert_seconds_to_time(data.get('effort',0)),
            'intro_video': None,
            'course_image_name': course_image_upload.name if course_image_upload else None,
            'course_image_asset_path': course_image_upload.location if course_image_upload else None,
            }
            CourseDetails.update_from_json(new_course.id, additional_info, self.creator)

            #SET GRADE
            grade = data.get('course_grade')/100.0
            CourseGradingModel.update_cutoffs_from_json(new_course_key, {"Pass":grade} ,self.creator)


            #TMA COURSEOVERVIEW
            if data.get('course_map'):
                course_map = json.loads(data.get('course_map'))
            else :
                course_map = ""
            data['course_about']=json.dumps({
                "description":data.get('short_description', ""),
                "course_map":json.loads(data.get('course_map', "")),
                "teacher_image":"/"+str(teacher_image_upload.location) if teacher_image_upload else "",
                "teacher_name":data.get('teacher_name', "") if data.get('teacher_name')!="null" else "",
                "teacher_email":data.get('teacher_email', "") if data.get('teacher_email')!="null" else "",
            })
            tmaOverviewFields=['is_manager_only', 'is_course_graded', 'is_mandatory', 'has_menu', 'tag', 'onboarding', 'course_about']
            tmaOverview = TmaCourseOverview.objects.filter(course_overview_edx__id=new_course.id).update(**{field:data.get(field) for field in tmaOverviewFields})
            
            return{"status":"success", "edit_link":reverse('course_handler', args=[str(new_course.id)]), "course_id":str(new_course.id)}
        except:
            return{"status":"error","details":"error while creating course"}

        