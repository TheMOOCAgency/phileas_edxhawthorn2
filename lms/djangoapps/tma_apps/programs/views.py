from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from openedx.core.djangoapps.util.maintenance_banner import add_maintenance_banner
from edxmako.shortcuts import render_to_response
from .helpers import programs_dashboard_context, TmaProgramManager


@login_required
@ensure_csrf_cookie
@add_maintenance_banner
def programs_dashboard_view(request):
    # Temporary renders course dashboard context
    context = programs_dashboard_context(request)
    response = render_to_response('tma_apps/programs_dashboard.html', context)
    return response

@login_required
@require_http_methods(["POST"])
def create_program(request):
    program_data = request.POST.copy()
    tma_program_creator = TmaProgramManager(request, program_data)
    new_program = tma_program_creator.create_new_program()

    status = 400 if new_program['status'] == 'error' else status = 200

    return JsonResponse(new_program, status = status)