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

from edxmako.shortcuts import render_to_response
from openedx.core.djangoapps.site_configuration.models import SiteConfiguration
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from student.views.dashboard import get_org_black_and_whitelist_for_site
from student.models import CourseEnrollment


log = logging.getLogger(__name__)


@login_required
def admin_homepage(request, *args, **kwargs):
    context = {}

    site_id = kwargs.get('id')
    context['site_id'] = site_id

    return render(request, '/tma_cms_apps/admin_hp.html', context)

def admin_faq(request, *args, **kwargs):
    context = {}
    site_id = kwargs.get('id')
    context['site_id'] = site_id

    return render(request, '/tma_cms_apps/admin_faq.html', context)

class SiteConfigurationDetailSerializer(serializers.ModelSerializer):
    values = serializers.JSONField()

    class Meta:
        model = SiteConfiguration
        fields = ['values']

    def get_values(self, obj):
        return json.dumps(obj.values)


class SiteConfigurationDetailViewSet(viewsets.ViewSet):
    '''
    Returns SiteConfiguration information for requested microsite.
    '''
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]
    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigurationDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        site_config = get_object_or_404(self.queryset, pk=kwargs.get('pk'))
        data = self.serializer_class(site_config).data

        return Response(data['values'])


class SiteConfigurationAPIView(generics.RetrieveUpdateAPIView):

    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigurationDetailSerializer

    def get(self, request, *args, **kwargs):
        site_config = self.queryset.get(pk=kwargs.get('pk'))
        data = {}
        if kwargs['section']:
            data = self.serializer_class(site_config).data['values'][kwargs.get('section')]

        return Response(data)

    def update(self, request, *args, **kwargs):
        site_config = self.queryset.get(pk=kwargs.get('pk'))

        data = self.serializer_class(site_config).data['values']

        if kwargs['section']:
            data[kwargs.get('section')] = request.data

        serializer = self.serializer_class(site_config, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class JSONCustomAPIView(generics.RetrieveUpdateAPIView):
    queryset = SiteConfiguration.objects.all()

    org_whitelist,org_blacklist = get_org_black_and_whitelist_for_site()
    current_organisation = "phileas"
    if org_whitelist:
         current_organisation = org_whitelist[0]

    def get(self, request, *args, **kwargs):
        urlSection = '/edx/var/edxapp/media/'+str(self.current_organisation) + '/'+ str(kwargs.get('section')) + '.json'
    	json_data = open(urlSection)
        data1 = json.load(json_data)
        return Response(data1)

    def update(self, request, *args, **kwargs):
        urlSection = '/edx/var/edxapp/media/'+str(self.current_organisation) + '/'+ str(kwargs.get('section')) + '.json'
        with open(urlSection, 'w') as f:
             json.dump(request.data, f)
        return Response(request.data)

"""
class SectionPerLangAPIView(generics.RetrieveUpdateAPIView):
    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigurationDetailSerializer

    def get(self, request, *args, **kwargs):
        site_config = self.queryset.get(pk=kwargs.get('pk'))
        data = {}

        if kwargs['section'] and kwargs['lang']:
            data = self.serializer_class(site_config).data['values'][kwargs['section']][kwargs['lang']]

        return Response(data)

    def update(self, request, *args, **kwargs):
        site_config = self.queryset.get(pk=kwargs.get('pk'))

        data = self.serializer_class(site_config).data['values']

        if kwargs['section']:
            data[kwargs['section']] = request.data
            log.info(data)

        serializer = self.serializer_class(site_config, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
"""
