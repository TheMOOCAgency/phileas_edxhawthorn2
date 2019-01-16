from openedx.features.course_experience.utils import get_course_outline_block_tree
from student.views.dashboard import get_course_enrollments
from tma_apps.models import TmaCourseEnrollment
from opaque_keys.edx.keys import CourseKey

import logging
log = logging.getLogger()

class Completion():
    def __init__(self,request):
        self.request = request

    def calculate_completion(self, course_id):
        total_blocks=0
        completed_blocks=0
        completion_rate=0
        course_key = CourseKey.from_string(course_id)
        course_sections = get_course_outline_block_tree(self.request,course_id).get('children')
        for section in course_sections :
          for subsection in section.get('children') :
            if subsection.get('children'):
                for unit in subsection.get('children'):
                  total_blocks+=1
                  if unit.get('complete'):
                    completed_blocks+=1

        completion_rate = float(completed_blocks)/total_blocks
        TmaCourseEnrollment.update_course_completion(course_key,self.request.user, completion_rate)
        return completion_rate

    def get_course_completion_rate(self, course_id):
        response={}
        response={
            'course_completion_rate':self.calculate_completion(course_id)
        }
        return response
