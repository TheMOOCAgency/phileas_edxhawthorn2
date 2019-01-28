"""
Useful Tma Methods
"""

def is_tma_staff(user):
    is_tma_staff=False
    if user.is_active and user.email.find('@themoocagency.com')>-1 and user.is_staff:
        is_tma_staff = True
    return is_tma_staff


def gather_course_info(course_id):
    
