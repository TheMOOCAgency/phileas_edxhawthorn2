import json
import logging
import os

from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import generics
from rest_framework.response import Response

from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from edxmako.shortcuts import render_to_response
from openedx.core.djangoapps.site_configuration.models import SiteConfiguration
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview


log = logging.getLogger(__name__)


def faq_view(request):
    context = {}
    url_section = '/edx/var/edxapp/media/america/faq.json'
    json_data = open(url_section)
    data1 = json.load(json_data)

    context['data'] = data1
    log.info(context)
    return render(request, '/tma_apps/faq.html',context )


