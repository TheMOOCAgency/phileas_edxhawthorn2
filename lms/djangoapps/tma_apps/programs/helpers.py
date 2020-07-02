### JC - PROGRAMS HELPERS ###

from .models import TmaProgramEnrollment, TmaProgramOverview, TmaProgramCourse
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from student.views.dashboard import _student_dashboard
from opaque_keys.edx.keys import CourseKey
from xmodule.modulestore.django import modulestore


# - use course context at the moment, will be removed once program context is set
def programs_dashboard_context(request):
    context = _student_dashboard(request)
    return context

class TmaProgramManager():
    def __init__(self, request, program_data):
        self.request = request
        self.program_data = program_data
        self.program_overview = _create_program_overview()


    def _create_program_overview(self):
        program_types = self.program_data['program_type']
        program_start_date = self.program_data['start_date']
        program_due_date = self.program_data['end_date']

        is_manager_only == True if 'is_manager_only' in program_types else is_manager_only == False
        is_mandatory == True if 'is_mandatory' in program_types else is_manager_only == False
        is_linear == True if 'is_linear' in program_types esle is_linear == False
        invitation_only == True if 'invitation_only' in program_types else invitation_only == False

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

        for index, course_key_string in enumerate(self.courses):
            self._create_program_course(course_key_string, index)

    
    def _create_program_course(self, course_key_string, index):
        # - course_details = {}
        # course_content = self._export_original_course_content(course_key_string)
        # self._import_content_to_duplicated_course(new_course_key_string)

        TmaProgramCourse.objects.create(
            program = self.program_overview,
            course = CourseOverview.objects.get(id=new_course_key_string),
            order = index
        )

    
    def _export_original_course_content(self, course_key_string):
        # course_key = CourseKey.from_string(course_key_string_string)
        # course_content = modulestore().get_course(course_key)

        # return course_content


    def _import_content_to_duplicated_course(self, new_course_key_string):
        # new_course_key = CourseKey.from_string(new_course_key_string)


    def create_new_program(self):
        try:
            self._create_program_overview()
            self._duplicate_original_courses()
            return { 'status':'success' }
        except:
            return { 'status':'error' }
