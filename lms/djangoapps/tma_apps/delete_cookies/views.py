from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
import logging

log = logging.getLogger()

@require_POST
@login_required
def tma_delete_cookies(request):
    #logout(request)
    response = HttpResponse()
    response.delete_cookie('openedx-language-preference')
    return response