import json
import logging
log = logging.getLogger()
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from edxmako.shortcuts import render_to_response

@login_required
@ensure_csrf_cookie
def quick_start(request):
    context={}
    #TRANSLATIONS
    translations = json.load(open("/edx/app/edxapp/edx-platform/cms/djangoapps/tma_cms_apps/quick_start/quick_start_trads.json"))
    context["translations"]=translations['fr']

    #CONFIG
    config = json.load(open("/edx/app/edxapp/edx-platform/cms/djangoapps/tma_cms_apps/quick_start/quick_start_config.json"))
    context.update(config)


    return render_to_response('/tma_cms_apps/quick_start.html', {"props":context})