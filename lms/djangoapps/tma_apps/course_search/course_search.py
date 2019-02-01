import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse

import logging

log = logging.getLogger()

def update_course_json(filepath, course_list):
    with open(filepath, 'r') as fp:
        data = json.load(fp)
    data = {}
    with open(filepath, 'w') as fp:
        json.dump(course_list, fp, indent=2)
    """
    try:
        with open(filepath, 'r') as fp:
            data = json.load(fp)
        data = {}
    except:
        log.warning('Cannot open JSON file')

    try:
        with open(filepath, 'w') as fp:
            json.dump(course_list, fp, indent=2)
            log.info('JSON file successfully updated')
    except:
        log.warning('Cannot update JSON file')
    """
    

@login_required
@require_POST
def search_courses(course_list, query):
    search_results = []    

    for course in course_list:
        for key in course:
            # Look for query in 3 fields only
            if key == 'tag' or key == 'short_description' or key == 'display_name':
                # Can't iterate if value is None
                if course[key] is not None:
                    if query in course[key]:
                        search_results.append(course)

    if len(search_results) == 0:
        search_results.append({
            'results': 'No results found'
        })
    
    return search_results