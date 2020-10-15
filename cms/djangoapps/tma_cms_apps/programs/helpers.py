### JC - PROGRAMS HELPERS ###

from cms.djangoapps.tma_cms_apps.programs.models import TmaProgramOverview, TmaProgramCourse
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from lms.djangoapps.tma_apps.models import TmaCourseEnrollment, TmaCourseOverview
from openedx.core.djangoapps.models.course_details import CourseDetails
from lms.djangoapps.courseware.courses import get_course_by_id
from cms.djangoapps.models.settings.course_metadata import CourseMetadata
from course_modes.models import CourseMode
from student.models import CourseEnrollment
from cms.djangoapps.contentstore.views.course import rerun_course
from opaque_keys.edx.keys import CourseKey
from xmodule.course_module import CourseFields
from xmodule.modulestore.django import modulestore
from xmodule.fields import Date
from random import randint


class TmaProgramManager():
    def __init__(self, request, program_data):
        self.request = request
        self.program_data = program_data
        self.is_manager_only = True if self.program_data['is_manager_only'] == 'true' else False
        self.is_mandatory = True if self.program_data['is_mandatory'] == 'true' else False
        self.is_linear = True if self.program_data['is_linear'] == 'true' else False
        self.invitation_only = True if self.program_data['invitation_only'] == 'true' else False
        self.program_overview = self._create_program_overview()

    def _create_program_overview(self):
        self.program_data['end_date'] = '' if self.program_data['end_date'] == 'null' else self.program_data['end_date']
        
        program_start_date = self.program_data['start_date']
        program_due_date = self.program_data['end_date']
        program_name = self.program_data['program_name']

        new_program_overview = TmaProgramOverview.objects.create(
            is_manager_only = self.is_manager_only,
            is_mandatory = self.is_mandatory,
            is_linear = self.is_linear,
            invitation_only = self.invitation_only,
            is_new = True,
            program_start_date = program_start_date,
            program_due_date = program_due_date,
            program_name = program_name
        )

        return new_program_overview


    def _duplicate_original_courses(self):
        courses = self.program_data['courses_list'].split(',')
        random_integer = str(randint(100000, 999999))
        for index, course_key_string in enumerate(courses):
            self._create_program_course(course_key_string, index, random_integer)

    
    def _create_program_course(self, course_key_string, index, random_integer):
        course_key = CourseKey.from_string(course_key_string)
        course = CourseOverview.objects.get(id=course_key)
        org = course.display_org_with_default
        number = course.display_number_with_default + random_integer
        run = 'duplicated' + random_integer
        display_name = course.display_name
        if self.program_data.has_key('start_date'):
            start = self.program_data['start_date']
        else:
            start = CourseFields.start.default
        fields = {'start': start}
        if display_name is not None:
            fields['display_name'] = display_name
        # cf. _create_or_rerun_course in course.py
        wiki_slug = u"{0}.{1}.{2}".format(org, number, run)
        fields['wiki_slug'] = wiki_slug
        new_course_key = rerun_course(self.request.user, course_key, org, number, run, fields, async=False)
        # update duplicated course dates depending on program dates
        date = Date()
        new_course = self._get_course_from_module_store(new_course_key)
        new_course.start = date.from_json(start)
        new_course.end = date.from_json(self.program_data['end_date'])
        module_store = modulestore()
        module_store.update_item(new_course, self.request.user.id)
        # update course metadata
        course = get_course_by_id(new_course_key)
        metadata = {'invitation_only': self.invitation_only}
        CourseMetadata.update_from_dict(metadata, course, self.request.user)
        # update TmaCourseOverview params depending on program params
        course_overview = CourseOverview.objects.get(id=new_course_key)
        TmaCourseOverview.objects.filter(course_overview_edx=course_overview).update(is_mandatory=self.is_mandatory, is_manager_only=self.is_manager_only, is_linear=self.is_linear)
        new_program_course = TmaProgramCourse.objects.get_or_create(
            program = self.program_overview,
            course = course_overview,
            order = index
        )
        return new_program_course
    
    def _get_course_from_module_store(self, course_key):
        ''' wait for course to be created in modulestore, to be improved '''
        module_store = modulestore()
        new_course = module_store.get_course(course_key)

        if new_course:
            return new_course
        else:
            return self._get_course_from_module_store(course_key)


    def create_new_program(self):
        try:
            self._duplicate_original_courses()
            return { 'status':'success' }
        except:
            return { 'status':'error' }

    def is_program_course(self):
        return True



