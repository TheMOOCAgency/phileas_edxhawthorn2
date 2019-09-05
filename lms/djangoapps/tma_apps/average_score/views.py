import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import ensure_csrf_cookie
from opaque_keys.edx.keys import CourseKey

from openedx.features.enterprise_support.api import data_sharing_consent_required

from courseware.courses import (
    get_course_with_access,
)
from lms.djangoapps.courseware.exceptions import CourseAccessRedirect, Redirect
from lms.djangoapps.grades.course_grade_factory import CourseGradeFactory
from lms.djangoapps.experiments.utils import get_experiment_user_metadata_context

from util.db import outer_atomic
from util.views import ensure_valid_course_key

from xmodule.modulestore.django import modulestore

from edxmako.shortcuts import render_to_response

# TMA IMPORTS
import xlrd
from collections import Counter
from operator import itemgetter
from openedx.features.course_experience.utils import get_course_outline_block_tree
from lms.djangoapps.instructor_task.models import ReportStore

log = logging.getLogger("edx.tma_apps")

@transaction.non_atomic_requests
@login_required
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@ensure_valid_course_key
@data_sharing_consent_required
def average(request, course_id):
    """ Display the progress/average score page. """
    course_key = CourseKey.from_string(course_id)

    with modulestore().bulk_operations(course_key):
        return _average(request, course_key)


def _average(request, course_key):

    course = get_course_with_access(request.user, 'load', course_key)
    student = User.objects.get(id=request.user.id)

    course_grade = CourseGradeFactory().read(student, course)
    courseware_summary = course_grade.chapter_grades.values()

    # TMA - retrieve display_name for all problems
    chapters_info = []
    blocks_info = []
    try:
        block_tree = get_course_outline_block_tree(request, str(course.id))
        for section in block_tree.get('children'):
            for chapter in section.get('children'):
                chapters_info.append({
                    'display_name': chapter['display_name'],
                    'total_grades': 0,
                    'attempted_students': 0
                })
                for unit in chapter.get('children'):
                    for item in unit.get('children'):
                        blocks_info.append({
                            'block_id': item['block_id'],
                            'display_name': item['display_name'],
                            'total_grades': 0,
                            'attempted_students': 0
                        })
    except:
        pass

    # TMA - read problem_grade report to calculate average grade per problem
    report_store = ReportStore.from_config(config_name='GRADES_DOWNLOAD')
    links = report_store.links_for(course.id)
    last_report_file = ''
    for link in links:
        if 'problem_grade_report' in link[0]:
            last_report_file = link[1]
            break

    if last_report_file:
        path = '/edx/var/edxapp' + str(last_report_file)
        _file = xlrd.open_workbook(path)
        report_data = _file.sheet_by_index(0)

        for i, block in enumerate(blocks_info):
            for j in range(1, report_data.ncols):
                # If col header corresponds to block display_name
                if block['display_name'] in report_data.cell(1, j).value:
                    # For every row (student)
                    for k in range(2, report_data.nrows):
                        # log.info(report_data.cell(k, j).value)
                        if 'Not Attempted' not in report_data.cell(k, j).value:
                            blocks_info[i]['total_grades'] += float(report_data.cell(k, j).value)
                            blocks_info[i]['attempted_students'] += 1

        for index, chapter in enumerate(chapters_info):
            for j in range(1, report_data.ncols):
                if chapter['display_name'] in report_data.cell(1, j).value:
                    for k in range(2, report_data.nrows):
                        if 'Not Attempted' not in report_data.cell(k, j).value:
                            log.info(report_data.cell(k, j).value)
                            chapter['total_grades'] += float(report_data.cell(k, j).value)
                            chapter['attempted_students'] += 1

    context = {
        'course': course,
        'courseware_summary': courseware_summary,
        'grade_summary': course_grade.summary,
        'student': student,
        'course_grade': course_grade,
        'chapters_info': chapters_info,
        'problems_info': blocks_info
    }

    context.update(
        get_experiment_user_metadata_context(
            course,
            student,
        )
    )

    with outer_atomic():
        response = render_to_response('tma_apps/average.html', context)

    return response