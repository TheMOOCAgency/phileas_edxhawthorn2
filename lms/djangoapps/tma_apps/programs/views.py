from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from openedx.core.djangoapps.util.maintenance_banner import add_maintenance_banner
from edxmako.shortcuts import render_to_response
from .helpers import programs_dashboard_context


@login_required
@ensure_csrf_cookie
@add_maintenance_banner
def programs_dashboard_view(request):
    context = programs_dashboard_context(request)
    response = render_to_response('tma_apps/programs_dashboard.html', context)
    return response