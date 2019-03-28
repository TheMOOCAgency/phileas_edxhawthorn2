from edxmako.shortcuts import render_to_response
import logging

log = logging.getLogger()

def global_zones_page(request):
    return render_to_response('tma_apps/zones_index.html')
