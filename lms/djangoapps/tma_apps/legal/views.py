from edxmako.shortcuts import render_to_response
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers

import logging

log = logging.getLogger()

def legal_notice_page(request):
    context = {}
    legal_content = ''
    try:
        if request.LANGUAGE_CODE == 'fr':
            legal_content = configuration_helpers.get_value('legal_content_fr')
        else:
            legal_content = configuration_helpers.get_value('legal_content_en')
        context = {
            "legal_content": legal_content
        }
    except:
        pass
    return render_to_response('tma_apps/legal.html', context)