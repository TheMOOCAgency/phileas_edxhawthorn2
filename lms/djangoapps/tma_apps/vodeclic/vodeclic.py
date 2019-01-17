from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from student.models import UserTestGroup, CourseEnrollment, UserProfile
import json
import requests
import hashlib
import datetime



def get_vodeclic_href(user,vodeclic_id):

    # Ensure the user is authenticated
    if not user.is_authenticated():
        return HttpResponseForbidden()
    else:
        if settings.FEATURES.get('TMA_VODECLIC_ENABLE'):
            date = datetime.datetime.now().strftime("%d%m%Y")
            api = 'uYUoVrzSEVityKwgNhHO'
            partenaire = 'LIkptrpdXajmLaJTRHYF'
            email = user.email
            first_name = user.first_name
            last_name = user.last_name
            id_membre = str(user.id)
            user_crypt = hashlib.sha256(id_membre+api).hexdigest()
            date_crypt = hashlib.sha256(date+api).hexdigest()
            url = 'https://lms.vodeclic.com/api/sso?'

            data_fr = 'partenaire='+partenaire+'&encrypted_id='+user_crypt+'&id='+id_membre+'&prenom='+first_name+'&nom='+last_name+'&email='+email+'&d='+date_crypt+'&vodeclic_id='+vodeclic_id+''
            href_sso = url+data_fr

            return href_sso

        else:
            return "TMA_VODECLIC_DISABLED"
