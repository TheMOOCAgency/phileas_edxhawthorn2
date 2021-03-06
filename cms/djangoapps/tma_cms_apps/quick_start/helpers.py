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
from models.settings.course_grading import CourseGradingModel
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from cms.djangoapps.contentstore.views.assets import update_course_run_asset
from courseware.courses import get_course_by_id
from opaque_keys.edx.keys import CourseKey
from models.settings.course_metadata import CourseMetadata
from contentstore.views.course import _refresh_course_tabs
from django.conf import settings
from django.urls import reverse
import urllib
from lms.djangoapps.courseware.courses import course_open_for_self_enrollment


class TmaCourseManager():
    def __init__(self, request, data, course_image=None, teacher_image=None,download_files=None,):
        self.request=request
        #self.creator = self._get_course_creator()
        self.creator = self.request.user
        self.data=data
        self.course_id=data["course_id"] if data['editMode']=="configure" else self._create_course_id()
        self.course_key =SlashSeparatedCourseKey.from_deprecated_string(self.course_id)
        self.course_image_upload=self._upload_image(course_image)
        self.teacher_image_upload=self._upload_image(teacher_image)
        self.download_files_upload=self._upload_multiple_files(download_files)
        self.tmaOverviewFields=['is_manager_only', 'is_course_graded', 'is_mandatory', 'has_menu', 'tag', 'onboarding', 'course_about','is_linear']

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
            'short_description': self.data.get('description'),
            'start_date':self.data.get('start_date', CourseFields.start.default),
            'end_date': self.data.get('end_date', CourseFields.end.default),
            'enrollment_start': self.data.get('start_date', CourseFields.start.default),
            'enrollment_end': self.data.get('end_date', CourseFields.end.default),
            'effort':self._convert_seconds_to_time(self.data.get('effort',0)),
            'intro_video': None,
        }

        if self.course_image_upload and not isinstance(self.course_image_upload, basestring):
            additional_info['course_image_name'] = self.course_image_upload.name
            additional_info['course_image_asset_path']= self.course_image_upload.location
        elif self.course_image_upload is None:
            additional_info['course_image_name'] = ""
            additional_info['course_image_asset_path']= ""

        CourseDetails.update_from_json(self.course_key, additional_info, self.creator)

    def _update_course_metadata(self):
        course=get_course_by_id(self.course_key)
        metadata={
            'invitation_only':self.data.get('invitation_only'),
            'display_name':self.data.get('course_name'),
            'self_paced':self.data.get('course_pacing')=="self_paced"
        }
        CourseMetadata.update_from_dict(metadata,course, self.creator)


    def _update_tma_course_overview(self):
        
        previous_course_about = TmaCourseOverview.get_tma_course_overview_by_course_id(self.course_key).course_about
        previous_course_about = json.loads(unicode(previous_course_about)) if previous_course_about else {}


        if self.data.get('course_map'):
            course_map = json.loads(self.data.get('course_map'))
        else :
            course_map = [{"title":"","subsections":[""]}]

        self.data['course_about']=json.dumps({
            "description":self.data.get('description', ""),
            "goals":self.data.get('course_goals', ""),
            "course_map":course_map,
            "teacher_image":"/"+str(self.teacher_image_upload.location) if (self.teacher_image_upload and not isinstance(self.teacher_image_upload, basestring)) else (self.teacher_image_upload if self.teacher_image_upload is not None else ""),
            "teacher_name":self.data.get('teacher_name', "") if self.data.get('teacher_name')!="null" else "",
            "teacher_email":self.data.get('teacher_email', "") if self.data.get('teacher_email')!="null" else "",
            "downloads": self.download_files_upload
            })
        tmaOverview = TmaCourseOverview.objects.get(course_overview_edx__id=self.course_key)
        TmaCourseOverview.objects.filter(course_overview_edx__id=self.course_key).update(**{field:self.data.get(field) for field in self.tmaOverviewFields if getattr(tmaOverview, field)!=self.data.get(field)})
    
    def _upload_image(self, imageFile):
        if imageFile and not isinstance(imageFile, basestring):
            fileUpload=update_course_run_asset(self.course_key, imageFile)
        elif isinstance(imageFile, basestring) and imageFile!="undefined":
            fileUpload=imageFile
        else:
            fileUpload=None
        return fileUpload

    def _upload_multiple_files(self, uploadFiles):
        fileUploads = []
        if uploadFiles :
            fileUploads = [
                {
                    "text":download_file['title'],
                    "link":"/"+str(update_course_run_asset(self.course_key, download_file['file']).location)
                }
                for download_file in uploadFiles
            ]

        if self.data.get('actual_course_downloads'):
            actual_course_downloads = json.loads(unicode(self.data['actual_course_downloads']))
            if actual_course_downloads and len(actual_course_downloads)>0:
                fileUploads+=actual_course_downloads

        return fileUploads




    def createUpdateCourse(self):
        try:
            self._update_course_overview()
            CourseGradingModel.update_cutoffs_from_json(self.course_key, {"Pass":(self.data.get('course_grade')/100.0)} ,self.creator)
            self._update_tma_course_overview()
            self._update_course_metadata()
            return{"status":"success", "edit_link":reverse('course_handler', args=[str(self.course_id)]), "course_id":str(self.course_id)}
        except:
            return{"status":"error"}







class TmaCourseInfo():
    def __init__(self, tmaOverview):
        self.tmaOverview = tmaOverview
        self.edxOverview = tmaOverview.course_overview_edx
        self.course_key = self.edxOverview.id
        self.course_id = str(self.course_key)
        self.org = self.edxOverview.org 
        self.lmsBase = str("https://"+self.org+"."+settings.LMS_BASE)

    def get_course_links(self):
        links={
            "configure_url":"#/configure/"+self.course_id,
            "statistics_url": self.lmsBase+"/login?next="+urllib.quote("/figures/course/"+self.course_id,''),
            "preview_url": self.lmsBase+"/login?next="+urllib.quote("/courses/"+self.course_id+"/about",'') if self.tmaOverview.is_vodeclic else self.lmsBase+"/login?next="+urllib.quote("/courses/"+self.course_id+"/courseware",''),
            "email_url":self.lmsBase+"/login?next="+urllib.quote("/courses/"+self.course_id+"/instructor",''),
            "rerun_url":"#/create/"+self.course_id,
            "contribute_url":reverse('course_handler', args=[self.course_id]),
        }
        return links

    def get_course_type(self):
        course_type=[]
        if self.tmaOverview.is_mandatory:
            course_type.append('is_mandatory')
        if self.tmaOverview.is_manager_only:
            course_type.append('is_manager_only')
        if self.tmaOverview.is_linear:
            course_type.append('is_linear')
        if self.get_course_metadata('invitation_only'):
            course_type.append('invitation_only')
        return course_type

    def get_course_about(self):
        try:
            course_about = json.loads(unicode(self.tmaOverview.course_about))
        except:
            course_about={}
        course_about.setdefault("course_map",[{"title":"","subsections":[""]}])
        course_about.setdefault("teacher_email","")
        course_about.setdefault("teacher_name","")
        course_about.setdefault("teacher_image","")
        course_about['course_goals']=course_about.get('goals') or ""
        course_about['actual_course_downloads']=course_about.get('downloads')
        return course_about

    def get_course_metadata(self, title):
        course=get_course_by_id(self.course_key)
        course_metadata = CourseMetadata.fetch_all(course)

        if title=="all":
            course_info={
                "course_grade":course.grade_cutoffs.get('Pass',0.5)*100,
                "language":course.language,
                "course_image":self.edxOverview.image_urls['large'] if not "static" in self.edxOverview.image_urls['large'] else "",
                "start_date": course.start,
                "end_date":course.end
            }
        elif title=="invitation_only":
            course_info=course_metadata['invitation_only']['value']
        return course_info
    
    def get_tmaOverview_info(self):
        tmaOverviewInfo={
            "tag":self.tmaOverview.tag,
            "is_new":self.tmaOverview.is_new,
            "onboarding":self.tmaOverview.onboarding,
            "type": 'vodeclic' if self.tmaOverview.is_vodeclic else 'phileas',
            "course_type":self.get_course_type(),
            "course_settings":self.get_course_settings()

        }
        return tmaOverviewInfo
    
    def get_course_settings(self):
        settings=[]
        if self.tmaOverview.has_menu:
            settings.append("has_menu")
        if self.tmaOverview.is_course_graded:
            settings.append("is_course_graded")
        return settings

    def get_detailed_status(self):
        status="open"
        if not self.tmaOverview.is_vodeclic and not course_open_for_self_enrollment(self.course_key):
            status="closed"
        return status

    def getBaseInfos(self):
        baseInfo={
            "course_id":self.course_id,
            "course_name":self.edxOverview.display_name,
            "course_pacing":"self_paced" if self.edxOverview.self_paced else "instructor_paced",
            "status":"self_paced" if self.edxOverview.self_paced else self.get_detailed_status(),
            "effort":self.edxOverview.effort.split(':') if self.edxOverview.effort else ['0','0'] ,
            "org":self.org,
            "description":self.edxOverview.short_description   
        }
        return baseInfo

    def getShortInfo(self):
        shortInfo=self.getBaseInfos()
        shortInfo.update(self.get_tmaOverview_info())
        shortInfo.update(self.get_course_links())
        return shortInfo

    def getDetailedInfo(self):
        detailedInfo = self.getShortInfo()
        detailedInfo.update(self.get_course_about())
        detailedInfo.update(self.get_course_metadata("all"))
        return detailedInfo

