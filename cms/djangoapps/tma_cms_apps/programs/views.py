from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .helpers import TmaProgramManager



@login_required
@require_http_methods(["POST"])
@csrf_exempt
def create_program(request):
    program_data = request.POST.copy()
    tma_program_creator = TmaProgramManager(request, program_data)
    new_program = tma_program_creator.create_new_program()

    status = 400 if new_program['status'] == 'error' else 200

    return JsonResponse(new_program, status=status)

@login_required
@require_http_methods(["POST"])
def enroll_program(request):
    enrollment_data = request.POST.copy()
    tma_program_enrollment = TmaProgramEnrollmentManager(request, enrollment_data)
    new_enrollment = tma_program_enrollment.create_new_program_enrollment()

    status = 400 if new_program['status'] == 'error' else 200

    return JsonResponse(new_enrollment, status=status)