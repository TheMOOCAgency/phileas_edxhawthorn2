### JC - PROGRAMS HELPERS ###

from .models import TmaProgramEnrollment, TmaProgramOverview, TmaProgramCourse
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from contentstore.views.course import rerun_course
from opaque_keys.edx.keys import CourseKey
from xmodule.course_module import CourseFields
from xmodule.modulestore.django import modulestore

from random import randint

class TmaProgramManager():
    def __init__(self, request, program_data):
        self.request = request
        self.program_data = program_data
        self.program_overview = _create_program_overview()


    def _create_program_overview(self):
        self.program_data['end_date'] = '' if self.program_data['end_date'] == 'null' else self.program_data['end_date']
        
        program_types = self.program_data['program_type']
        program_start_date = self.program_data['start_date']
        program_due_date = self.program_data['end_date']

        is_manager_only = True if 'is_manager_only' in program_types else False
        is_mandatory = True if 'is_mandatory' in program_types else False
        is_linear = True if 'is_linear' in program_types else False
        invitation_only = True if 'invitation_only' in program_types else False

        new_program_overview = TmaProgramOverview.objects.create(
            is_manager_only = is_manager_only,
            is_mandatory = is_mandatory,
            is_linear = is_linear,
            invitation_only = invitation_only,
            is_new = True,
            program_start_date = program_start_date,
            program_due_date = program_due_date
        )

        return new_program_overview


    def _duplicate_original_courses(self):
        courses = program_data['courses_list']

        for index, course_key_string in enumerate(courses):
            self._create_program_course(course_key_string, index)

    
    def _create_program_course(self, course_key_string, index):
        course_key = CourseKey.from_string(course_key_string)
        course = CourseOverview.objects.get(id=course_key)

        random_integer = randint(100000, 999999)
        org = course.display_org_with_default
        number = course.display_number_with_default + random_integer
        run = 'duplicated' + random_integer
        display_name = course.display_name

        if self.program_data['start_date']:
            start = self.program_data['start_date']
        else:
            start = CourseFields.start.default

        fields = {'start': start}
        if display_name is not None:
            fields['display_name'] = display_name

        # cf. _create_or_rerun_course in course.py
        wiki_slug = u"{0}.{1}.{2}".format(org, number, run)
        fields['wiki_slug'] = wiki_slug

        new_course_key = rerun_course(self.request.user, course_key, org, number, run, fields)

        TmaProgramCourse.objects.create(
            program = self.program_overview,
            course = CourseOverview.objects.get(id=new_course_key),
            order = index
        )


    def create_new_program(self):
        try:
            self._duplicate_original_courses()
            return { 'status':'success' }
        except:
            return { 'status':'error' }
