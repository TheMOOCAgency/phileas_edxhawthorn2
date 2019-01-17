from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from student.models import UserTestGroup, CourseEnrollment, UserProfile
import json
import requests
import hashlib
import datetime

def get_sspeaking_href(user):
    # Ensure the user is authenticated
    if not user.is_authenticated():
        return HttpResponseForbidden()
    else:
        # TODO : restore the feature flag
        #if settings.FEATURES.get('TMA_SSPEAKING_ENABLE'):
        if True:
            first_name = user.first_name
            last_name = user.last_name
            email = user.email
            key = '39D02FA5A62B2A62CEA0551EC69E80FA'
            groupe = 'AMUNDI'
            id_interne = str(user.id)
            url = 'https://www.lms.7speaking.com/7sautolog.cfm?'
            data_fr = 'prenom='+first_name+'&nom='+last_name+'&email='+email+'&key='+key+'&groupe='+groupe+'&id_interne='+id_interne
            href_sso = url+data_fr
            return href_sso
        else:
            return "TMA_SSPEAKING_DISABLED"

