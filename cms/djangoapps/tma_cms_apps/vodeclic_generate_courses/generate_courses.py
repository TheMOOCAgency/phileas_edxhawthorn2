import requests
import hashlib
import datetime
import urllib
import os
import json
from contentstore.views.course import create_new_course
from contentstore.views.assets import update_course_run_asset
from django.contrib.auth.admin import User
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from openedx.core.djangoapps.models.course_details import CourseDetails
from lms.djangoapps.courseware.courses import get_course_by_id
from util.organizations_helpers import (
    add_organization_course,
    get_organization_by_short_name,
    organizations_enabled,
)
from .helpers import store_jacket_image
from xmodule.modulestore.exceptions import DuplicateCourseError
from lms.djangoapps.tma_apps.models import TmaCourseOverview

import pytz
utc=pytz.UTC

import logging
log = logging.getLogger()





class VodeclicGenerator():
    def __init__(self):
        self.api_key='uYUoVrzSEVityKwgNhHO'
        self.partenaire='LIkptrpdXajmLaJTRHYF'
        self.encrypted_partenaire =hashlib.sha256(self.partenaire+self.api_key).hexdigest()
        self.url_base='https://lms.vodeclic.com/api'
        self.date_today=datetime.datetime.now()
        self.vodeclic_img_path_base='/edx/app/edxapp/edx-platform/cms/static/tma-cms-static/vodeclic-course-images/images_'

    def _get_json_file(self, language):
        if language=="fr":
            file_directory=os.path.dirname(__file__)+'/vodeclic_fr_courses.json'
        else :
            file_directory=os.path.dirname(__file__)+'/vodeclic_en_courses.json'
        return file_directory

    def _get_vodeclic_courses(self,language):
        #LOCAL JSON
        file_directory=self._get_json_file(language)
        json_data=open(file_directory).read()
        data = json.loads(json_data)
        vodeclic_courses=data.get('data',{}).get('subject',{})
        return vodeclic_courses

    def update_vodeclic_json(self, language):
        file_directory=self._get_json_file(language)
        url_catalog=self.url_base+'/catalogue.json?'
        params = dict(
            partenaire=self.partenaire,
            encrypted_partenaire=self.encrypted_partenaire,
            lang=language,
        )
        resp = requests.get(url=url_catalog, params=params)
        vodeclic_courses_list = resp.json()
        with open(file_directory, 'w') as file:
            file.write(vodeclic_courses_list)


    def _get_course_creator(self):
        try:
            vodeclic_user = User.objects.get(username='coursecreator')
        except User.DoesNotExist:
            vodeclic_user = User.objects.create(
                username='coursecreator',
                email='coursecreator@tma.com',
                first_name='coursecreator',
                last_name='coursecreator',
                is_active=True,
                is_staff=True
            )
            vodeclic_user.set_password('coursecreator')
            vodeclic_user.save()
        return vodeclic_user

    def _set_org_info(self, course_id,org='phileas'):
        org_data = get_organization_by_short_name(org)
        add_organization_course(org_data, course_id)

    def save_all_courses_pictures(self, language):
        vodeclic_courses = self._get_vodeclic_courses(language)
        log.info('Gathering pictures for courses of language {}'.format(language))
        for vodeclic_course_params in vodeclic_courses :
            vodeclic_picture = vodeclic_course_params.get('large_image_png_url')
            vodeclic_language=vodeclic_course_params.get('language')
            vodeclic_id=vodeclic_course_params.get('id')
            self._save_picture_from_url(vodeclic_picture, self.vodeclic_img_path_base+vodeclic_language+'/'+vodeclic_id+'.png')
        log.info('END - Gathering pictures for courses of language {}'.format(language))

    def _save_picture_from_url(self, picture_url, file_path):
        urllib.urlretrieve(picture_url, file_path)

    def convert_seconds_to_edx_time(self, seconds):
        minutes = int(seconds) // 60
        hours = minutes // 60
        rest_minutes = minutes % 60
        return str(hours)+":"+str(rest_minutes)

    def update_vodeclic_courses(self, vodeclic_id_list, org='phileas', language='en'):
        vodeclic_courses = self._get_vodeclic_courses(language)
        courses_to_create=[]
        log.info('Importing course for language {}'.format(language))
        for vodeclic_course_params in vodeclic_courses :
            if vodeclic_course_params.get('id') in vodeclic_id_list.keys() :
                log.info('Importing course {}'.format(vodeclic_course_params.get('title')))
                vodeclic_language=vodeclic_course_params.get('language')
                vodeclic_run="Vodeclic_"+vodeclic_language
                vodeclic_number=vodeclic_course_params.get('id')
                vodeclic_user=self._get_course_creator()
                vodeclic_id=vodeclic_course_params.get('id')
                vodeclic_picture = vodeclic_course_params.get('large_image_png_url')
                course_already_exist=False

                #Build fields list
                fields= {
                "display_name": vodeclic_course_params.get('title'),
                "start": self.date_today.replace(tzinfo=utc),
                "enrollment_start":self.date_today.replace(tzinfo=utc),
                }

                #Create course
                try:
                    vodeclic_course=create_new_course(user=vodeclic_user, org=org, number=vodeclic_number, run=vodeclic_run,fields=fields)
                except DuplicateCourseError:
                    vodeclic_course_key = SlashSeparatedCourseKey.from_deprecated_string('course-v1:'+org+'+'+vodeclic_number+'+'+vodeclic_run)
                    vodeclic_course = get_course_by_id(vodeclic_course_key)
                    course_already_exist=True


                #Set organization
                self._set_org_info(org, vodeclic_course.id)

                #Save Image
                #self._save_picture_from_url(vodeclic_picture, self.vodeclic_img_path_base+vodeclic_language+'/'+vodeclic_id+'.png')
                try:
                    vodeclic_image_name, vodeclic_image_asset_path = store_jacket_image(
                        vodeclic_course.id, self.vodeclic_img_path_base+vodeclic_language+'/',
                        vodeclic_id + ".png"
                    )
                except:
                    pass

                if course_already_exist:
                    additional_info={
                    'course_image_name': vodeclic_image_name,
                    'course_image_asset_path': vodeclic_image_asset_path,
                    }
                else :
                    #Add other course info
                    additional_info = {
                    'display_name': vodeclic_course_params.get('title'),
                    'language': vodeclic_course_params.get('language'),
                    'short_description': vodeclic_course_params.get('description'),
                    'intro_video': None,
                    'course_image_name': vodeclic_image_name,
                    'course_image_asset_path': vodeclic_image_asset_path,
                    'start_date': vodeclic_course.start.replace(tzinfo=utc),
                    'end_date': vodeclic_course.end,
                    'enrollment_start': vodeclic_course.start.replace(tzinfo=utc),
                    'enrollment_end': vodeclic_course.end,
                    'effort':self.convert_seconds_to_edx_time(vodeclic_course_params.get('duration'))
                    }

                CourseDetails.update_from_json(vodeclic_course.id, additional_info, vodeclic_user)
                #Get or create TmaCourseOverview
                TmaCourseOverview.add_vodelic_course(SlashSeparatedCourseKey.from_deprecated_string(str(vodeclic_course.id)), vodeclic_id_list[vodeclic_id].get('tags'))

                log.info('{} imported'.format(vodeclic_course_params.get('title')))
