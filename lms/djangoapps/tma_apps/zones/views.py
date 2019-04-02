from edxmako.shortcuts import render_to_response
from django.shortcuts import redirect
from django.conf import settings

import logging

log = logging.getLogger()

def global_zones_page(request):
    next_param = request.GET.get('next', '')
    context = {}

    # If user not logged in : buttons lead to SSO
    if not request.user.is_authenticated:
        context = {
            'sso_europe': '/auth/login/amundi/?auth_entry=login&next=europe.'+ settings.SITE_NAME +'%2F'+ next_param,
            'sso_americas': '/auth/login/amundi/?auth_entry=login&next=americas.'+ settings.SITE_NAME +'%2F'+ next_param,
            'sso_asia': '/auth/login/amundi/?auth_entry=login&next=asia.'+ settings.SITE_NAME +'%2F'+ next_param
        }
        return render_to_response('tma_apps/zones_index.html', context)
    else:
        return redirect('/dashboard')
