# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
from courseware.courses import get_course_by_id



class TmaProgramOverview(models.Model):
    is_manager_only = models.BooleanField(default=False)
    is_mandatory = models.BooleanField(default=False)
    is_linear = models.BooleanField(default=False)
    invitation_only = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    program_start_date = models.DateTimeField(db_index=True, null=True)
    program_due_date = models.DateTimeField(db_index=True, null=True)
    program_name = models.CharField(default='program name',max_length=50)

class TmaProgramCourse(models.Model):
    program = models.ForeignKey(TmaProgramOverview, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseOverview, on_delete=models.CASCADE, unique=True)
    order = models.IntegerField(default=0)

    @classmethod
    def is_program_course(cls, course_id):
        try:
            course_overview = CourseOverview.objects.get(id=course_id)
            program_course = TmaProgramCourse.objects.get(course=course_overview)
            return True
        except cls.DoesNotExist:
            return False

    @classmethod
    def get_all_courses_from_program(cls, course_id):
        courses_list = []
        is_program_course = cls.is_program_course(course_id)
        
        if is_program_course:
            course_overview = CourseOverview.objects.get(id=course_id)
            program_course_overview = TmaProgramCourse.objects.get(course=course_overview)
            all_overviews = TmaProgramCourse.objects.filter(program=program_course_overview.program).order_by('order')

            for overview in all_overviews:
                courses_list.append(get_course_by_id(overview.course.id))
        
        else:
            courses_list.append(get_course_by_id(course_id))

        return courses_list

    @classmethod
    def get_program_details(cls, course_id):
        course_overview = CourseOverview.objects.get(id=course_id)
        program_course_overview = TmaProgramCourse.objects.get(course=course_overview)
        program = program_course_overview.program
        
        return program



