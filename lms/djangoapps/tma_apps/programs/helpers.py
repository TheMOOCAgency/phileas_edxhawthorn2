### JC - PROGRAM HELPERS ###

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from openedx.core.djangoapps.util.maintenance_banner import add_maintenance_banner

@login_required
@ensure_csrf_cookie
@add_maintenance_banner
def program_dashboard(request):
    context = {}
    return context