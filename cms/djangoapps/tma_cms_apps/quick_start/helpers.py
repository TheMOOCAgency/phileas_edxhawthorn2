import logging
log = logging.getLogger()

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


class TmaCourseCreator():
    def __init__(self):
        self.creator = self._get_course_creator()

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


    def createCourse(self, data):
        try:
            #CREATE COURSE
            fields= {
            "display_name": data.get('course_name'),
            "start": data.get('start_date', CourseFields.start.default),
            "enrollment_start": data.get('start_date', CourseFields.start.default),
            }
            new_course = create_new_course(user=self.creator, org=data.get('org'), number=data.get('course_number'), run=data.get('course_session'),fields=fields)

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
            'course_image_name': None,
            'course_image_asset_path': None,
            }
            CourseDetails.update_from_json(new_course.id, additional_info, self.creator)

            #TMA COURSEOVERVIEW
            tmaOverviewFields=['is_manager_only', 'is_course_graded', 'is_mandatory', 'has_menu', 'is_course_graded', 'tag', 'onboarding']
            tmaOverview = TmaCourseOverview.objects.filter(course_overview_edx__id=new_course.id).update(**{field:data.get(field) for field in tmaOverviewFields})
            return{"status":"success", "edit_link":reverse('course_handler', args=[str(new_course.id)])}
        except:
            return{"status":"error","details":"error while creating course"}

        