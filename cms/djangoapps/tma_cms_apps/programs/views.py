from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .helpers import TmaProgramManager
import logging

log = logging.getLogger()


@login_required
@require_http_methods(["POST"])
def create_program(request):
    program_data = request.POST.copy()
    tma_program_creator = TmaProgramManager(request, program_data)
    new_program = tma_program_creator.create_new_program()

    status = 400 if new_program['status'] == 'error' else 200

    return JsonResponse(new_program, status=status)
