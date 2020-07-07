### JC - PROGRAMS HELPERS ###

from .models import TmaProgramEnrollment, TmaProgramOverview, TmaProgramCourse
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from lms.djangoapps.tma_apps.models import TmaCourseEnrollment, TmaCourseOverview
from openedx.core.djangoapps.models.course_details import CourseDetails
from courseware.courses import get_course_by_id
from cms.djangoapps.models.settings.course_metadata import CourseMetadata
from course_modes.models import CourseMode
from student.models import CourseEnrollment
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
        
        program_type = self.program_data['program_type']
        program_start_date = self.program_data['start_date']
        program_due_date = self.program_data['end_date']

        is_manager_only = True if 'is_manager_only' in program_type else False
        is_mandatory = True if 'is_mandatory' in program_type else False
        is_linear = True if 'is_linear' in program_type else False
        invitation_only = True if 'invitation_only' in program_type else False

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

        course_overview = CourseOverview.objects.get(id=new_course_key)

        # update course details depending on program details
        course_details = CourseDetails.objects.get(course_id=new_course_key)
        course_detail.start = start
        course_detail.end = self.program_data['end_date']
        course_detail.save()
        
        course = get_course_by_id(self.new_course_key)
        invitation_only = True if 'invitation_only' in self.program_data['program_type'] else False
        metadata = {'invitation_only': invitation_only}
        CourseMetadata.update_from_dict(metadata, course, self.request.user)
        
        tma_course_overview = TmaCourseOverview.objects.get(course_overview_edx=course_overview)
        tma_course_overview.is_manager_only = True if 'is_manager_only' in self.program_data['program_type'] else False
        tma_course_overview.is_linear = True if 'is_linear' in self.program_data['program_type'] else False
        tma_course_overview.is_mandatory = True if 'is_mandatory' in self.program_data['program_type'] else False
        tma_course_overview.save()

        TmaProgramCourse.objects.create(
            program = self.program_overview,
            course = course_overview,
            order = index
        )


    def create_new_program(self):
        try:
            self._duplicate_original_courses()
            return { 'status':'success' }
        except:
            return { 'status':'error' }


class TmaProgramEnrollmentManager():
    def __init__(self, request, enrollment_data):
        self.request = request
        self.enrollment_data = enrollment_data
        self.program = TmaProgramOverview.objects.get(id=self.enrollment_data.program_id)
        self.courses = TmaProgramCourse.objects.filter(program=program)


    def _enroll_program_courses(self):
        ''' Enroll invidually to all program courses '''

        for course in self.courses:
            course_key = course.course_id

            available_modes = CourseMode.modes_for_course_dict(course_key)

            if CourseMode.can_auto_enroll(course_key):
                enroll_mode = CourseMode.auto_enroll_mode(course_key, available_modes)

                if enroll_mode:
                    CourseEnrollment.enroll(self.request.user, course_key, check_access=True, mode=enroll_mode)


    def get_program_completion_rate(self):
        ''' Calculate the average of program courses completion rates '''
        total_rates = 0
        global_average = 0

        for course in self.courses:
            course_key = course.id

            total_rates += TmaCourseEnrollment.objects.get(course_enrollment_edx__course_id=course_key, course_enrollment_edx__user_id=self.request.user.id).completion_rate
        
        global_average = total_rates / len(self.courses)

        return global_average


    def create_new_program_enrollment(self):
        try:
            _enroll_program_courses()

            TmaProgramEnrollment.objects.create(
                user = self.request.user,
                program = self.program,
                enrollment_date = datetime.now(),
                has_started_program = True,
                has_validated_program = False,
                program_completion_rate = 0
            )

            return { 'status':'success' }

        except:

            return { 'status':'error' }