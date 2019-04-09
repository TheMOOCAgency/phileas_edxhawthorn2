from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from student.models import UserTestGroup, CourseEnrollment, UserProfile
import hashlib
import datetime

import logging
log = logging.getLogger()



def get_vodeclic_href(user, course_id):
    api_key='uYUoVrzSEVityKwgNhHO'
    partenaire='LIkptrpdXajmLaJTRHYF'
    encrypted_partenaire =hashlib.sha256(partenaire+api_key).hexdigest()
    url_base='https://lms.vodeclic.com/api'
    date=datetime.datetime.now().strftime("%d%m%Y")
    if user.is_authenticated():
        vodeclic_id_arg = 'vodeclic_id='+str(course_id).split('+')[1]
        partenaire_arg='&partenaire='+partenaire
        encrypted_user_arg='&encrypted_id='+hashlib.sha256(str(user.profile.rpid)+api_key).hexdigest()
        user_id_arg='&id='+str(user.profile.rpid)
        prenom_arg='&prenom='+user.first_name
        nom_arg='&nom='+user.last_name
        email_arg='&email='+user.email
        date_arg='&d='+hashlib.sha256(date+api_key).hexdigest()
        return url_base+'/sso?'+vodeclic_id_arg+partenaire_arg+encrypted_user_arg+user_id_arg+prenom_arg+nom_arg+email_arg+date_arg
    else :
        return HttpResponseForbidden()
