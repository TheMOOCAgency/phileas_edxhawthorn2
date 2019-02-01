from django.http import JsonResponse

import logging

log = logging.getLogger()

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