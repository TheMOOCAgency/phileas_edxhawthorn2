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
from courseware.courses import get_course_by_id
from opaque_keys.edx.keys import CourseKey
from models.settings.course_metadata import CourseMetadata
from contentstore.views.course import _refresh_course_tabs



class TmaCourseCreator():
    def __init__(self, request, user, data, course_image=None, teacher_image=None,download_files=None):
        self.request=request
        #self.creator = self._get_course_creator()
        self.creator = user
        self.data=data
        self.course_id=data["course_id"] if data['editMode']=="configure" else self._create_course_id()
        self.course_key =SlashSeparatedCourseKey.from_deprecated_string(self.course_id)
        self.course_image_upload=self._upload_image(course_image)
        self.teacher_image_upload=self._upload_image(teacher_image)
        self.download_files_upload=self._upload_multiple_files(download_files)
        self.tmaOverviewFields=['is_manager_only', 'is_course_graded', 'is_mandatory', 'has_menu', 'tag', 'onboarding', 'course_about']

    def _create_course_id(self):
        fields= {
            "display_name": self.data.get('course_name'),
            "start": self.data.get('start_date', CourseFields.start.default),
            "enrollment_start": self.data.get('start_date', CourseFields.start.default),
        }
        new_course = create_new_course(
            user=self.creator, 
            org=self.data.get('org'), 
            number=self.data.get('course_number'), 
            run=self.data.get('course_session'),fields=fields
        )
        return str(new_course.id)

    def _convert_seconds_to_time(self, seconds):
        minutes = int(seconds) // 60
        hours = minutes // 60
        rest_minutes = minutes % 60
        return str(hours)+":"+str(rest_minutes)

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

    def _update_course_overview(self):
        additional_info = {
            'display_name': self.data.get('course_name'),
            'language': self.data.get('language'),
            'short_description': self.data.get('short_description'),
            'start_date':self.data.get('start_date', CourseFields.start.default),
            'end_date': self.data.get('end_date', CourseFields.end.default),
            'enrollment_start': self.data.get('start_date', CourseFields.start.default),
            'enrollment_end': self.data.get('end_date', CourseFields.end.default),
            'effort':self._convert_seconds_to_time(self.data.get('effort',0)),
            'intro_video': None,
            'course_image_name': self.course_image_upload.name if self.course_image_upload else None,
            'course_image_asset_path': self.course_image_upload.location if self.course_image_upload else None,
            'self_paced':self.data.get('course_pacing')=="self_paced"
        }
        CourseDetails.update_from_json(self.course_key, additional_info, self.creator)

    def _update_course_metadata(self):
        course=get_course_by_id(self.course_key)
        metadata={
            'invitation_only':self.data.get('invitation_only')
        }
        CourseMetadata.update_from_dict(metadata,course, self.creator)


    def _update_tma_course_overview(self):
        tmaOverview = TmaCourseOverview.objects.filter(course_overview_edx__id=self.course_key)

        if self.data.get('course_map'):
            course_map = json.loads(self.data.get('course_map'))
        else :
            course_map = ""

        self.data['course_about']=json.dumps({
            "description":self.data.get('short_description', ""),
            "course_map":json.loads(self.data.get('course_map', "")),
            "teacher_image":"/"+str(self.teacher_image_upload.location) if self.teacher_image_upload else "",
            "teacher_name":self.data.get('teacher_name', "") if self.data.get('teacher_name')!="null" else "",
            "teacher_email":self.data.get('teacher_email', "") if self.data.get('teacher_email')!="null" else "",
            "downloads": self.download_files_upload if self.download_files_upload else ""
        })
        tmaOverview.update(**{field:self.data.get(field) for field in self.tmaOverviewFields})
    
    def _upload_image(self, imageFile):
        fileUpload=update_course_run_asset(self.course_key, imageFile) if imageFile else None
        return fileUpload

    def _upload_multiple_files(self, uploadFiles):
        fileUploads = None
        if uploadFiles :
            fileUploads = [
                {
                    "text":download_file['title'],
                    "link":"/"+str(update_course_run_asset(self.course_key, download_file['file']).location)
                }
                for download_file in self.download_files
            ]
        return fileUploads




    def createUpdateCourse(self):
        #try:
        self._update_course_overview()
        CourseGradingModel.update_cutoffs_from_json(self.course_key, {"Pass":(self.data.get('course_grade')/100.0)} ,self.creator)
        self._update_tma_course_overview()
        self._update_course_metadata()
        return{"status":"success", "edit_link":reverse('course_handler', args=[str(self.course_id)]), "course_id":str(self.course_id)}
        #except:
        #return{"status":"error"}

        