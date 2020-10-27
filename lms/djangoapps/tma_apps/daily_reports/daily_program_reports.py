# -*- coding: utf-8 -*-
import sys
import csv
import os
import json
import logging
import importlib

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lms.envs.aws")
os.environ.setdefault("lms.envs.aws,SERVICE_VARIANT", "lms")
os.environ.setdefault("PATH", "/edx/app/edxapp/venvs/edxapp/bin:/edx/app/edxapp/edx-platform/bin:/edx/app/edxapp/.rbenv/bin:/edx/app/edxapp/.rbenv/shims:/edx/app/edxapp/.gem/bin:/edx/app/edxapp/edx-platform/node_modules/.bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin")

os.environ.setdefault("SERVICE_VARIANT", "lms")
os.chdir("/edx/app/edxapp/edx-platform")

startup = importlib.import_module("lms.startup")
startup.run()
log = logging.getLogger()

from cms.djangoapps.tma_cms_apps.programs.models import TmaProgramCourse
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from student.models import CourseEnrollment
from lms.djangoapps.instructor_task.tasks_helper.grades import ProblemGradeReport


def get_courses_ids_list():
    """
    Get courses ids for courses with
    more than 100 enrollments and 
    program courses, as we want to 
    generate reports for them only.
    """

    courses = CourseOverview.objects.all()
    selected_course_ids = []

    for course in courses:
        course_id = course.id
        is_program_course = TmaProgramCourse.is_program_course(course_id)

        if is_program_course:
            index = TmaProgramCourse(course=course).order
            if index == 0:
                selected_course_ids.append(course_id)
        else:
            total_enrollments = len(CourseEnrollment.objects.filter(course=course))
            log.info(total_enrollments)
            if total_enrollments >= 100:
                selected_course_ids.append(course_id)
                log.info("Test")

    return selected_course_ids


def generate_reports():
    """ 
    Generate grades report for 
    selected courses and programs.
    """

    ids = get_courses_ids_list()

    for id in ids:
        try:
            ProblemGradeReport.generate(None, None, id, None, 'graded')
        except:
            pass
        

generate_reports()
