### JC - PROGRAMS HELPERS ###

from student.views.dashboard import _student_dashboard
from opaque_keys.edx.keys import CourseKey
from xmodule.modulestore.django import modulestore


# - use course context at the moment, will be removed once program context is set
def programs_dashboard_context(request):
    context = _student_dashboard(request)
    return context

class TmaProgramManager():
    def __init__(self, courses):
        self.courses = courses

    def duplicate_original_courses(self):
        for course_key_string in self.courses:
            create_program_course(course_key_string)
    
    def create_program_course(self, course_key_string):
        # - course_details = {}
        course_content = export_original_course_content(course_key_string)
        # - import_content_to_duplicated_course()
    
    def export_original_course_content(self, course_key_string):
        course_key = CourseKey.from_string(course_key_string_string)
        course_content = modulestore().get_course(course_key)
        return course_content

    
    def import_content_to_duplicated_course(self, new_course_key_string):
        new_course_key = CourseKey.from_string(new_course_key_string)