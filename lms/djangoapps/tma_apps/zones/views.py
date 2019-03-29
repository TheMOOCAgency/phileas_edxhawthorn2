from edxmako.shortcuts import render_to_response
from django.shortcuts import redirect

import logging

log = logging.getLogger()

def global_zones_page(request):
    next_param = request.GET.get('next', '')
    context = {}
    # If user not logged in : buttons lead to SSO
    if not request.user.is_authenticated:
        context = {
            'sso_europe': '/auth/login/amundi/?auth_entry=login&next=%2Fdashboard&zone=europe',
            'sso_americas': '/auth/login/amundi/?auth_entry=login&next=%2Fdashboard&zone=americas',
            'sso_asia': '/auth/login/amundi/?auth_entry=login&next=%2Fdashboard&zone=asia'
        }
        return render_to_response('tma_apps/zones_index.html', context)
    else:
        return redirect('/dashboard')
