from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import JsonResponse

from opaque_keys.edx.keys import CourseKey

from .certificate import certificate
from student.models import CourseEnrollment
from lms.djangoapps.tma_apps.models import TmaCourseEnrollment

import logging
log = logging.getLogger()


@login_required
@require_GET
def ensure(request,course_id):
    course_key = CourseKey.from_string(course_id)
    return JsonResponse(certificate(request.user).check_course_certificate(course_key))

@login_required
@require_GET
def render(request,course_id):
    course_key = CourseKey.from_string(course_id)
    return certificate(request.user).view(course_key)

@login_required
@require_POST
def check_best_grade(request, course_id):
    course_key = CourseKey.from_string(course_id)
    learner_email = request.POST.get('email', '')

    if User.objects.filter(email=learner_email).exists():
        learner = User.objects.get(email=learner_email)
        
        if CourseEnrollment.objects.filter(course_id=course_key, user_id=learner.id).exists():
            tma_ce = TmaCourseEnrollment.objects.get(course_enrollment_edx__user_id=learner.id, course_enrollment_edx__course_id=course_key)

            return JsonResponse({
                'best_grade': tma_ce.best_student_grade
            })
        else:
            return JsonResponse({'error': 'Learner is not enrolled in this course.'})
    else:
        return JsonResponse({'error': 'We couldn\'t find a learner matching this email.'})

@login_required
@require_GET
def generate(request, course_id):
    course_key = CourseKey.from_string(course_id)

    learner_email = request.GET.get('email', '')
    learner_score = request.GET.get('score', '')
    learner = User.objects.get(email=learner_email)

    return certificate(learner).generate(course_key, int(learner_score))