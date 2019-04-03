from edxmako.shortcuts import render_to_response
from django.shortcuts import redirect
from django.conf import settings

import logging

log = logging.getLogger()

def global_zones_page(request):
    next_param = request.GET.get('next', '')
    context = {}

    context = {
        'sso_europe': 'https://europe.' + settings.SITE_NAME + '/auth/login/amundi/?auth_entry=login&next=europe.'+ settings.SITE_NAME + next_param,
        'sso_americas': 'https://americas.' + settings.SITE_NAME + '/auth/login/amundi/?auth_entry=login&next=americas.'+ settings.SITE_NAME + next_param,
        'sso_asia': 'https://asia.' + settings.SITE_NAME + '/auth/login/amundi/?auth_entry=login&next=asia.'+ settings.SITE_NAME + next_param
    }

    return render_to_response('tma_apps/zones_index.html', context)