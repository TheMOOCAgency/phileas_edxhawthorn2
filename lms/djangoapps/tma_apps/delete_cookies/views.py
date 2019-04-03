from edxmako.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
import logging

log = logging.getLogger()

@require_GET
@login_required
def tma_delete_cookies(request):
    response = redirect('/')
    return response