import json
import logging

from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import generics
from rest_framework.response import Response

from openedx.core.djangoapps.site_configuration.models import SiteConfiguration

log = logging.getLogger(__name__)


@ensure_csrf_cookie
@login_required
def admin_homepage(request):
    log.info('TOTOOTO')
    return render(request, '/tma_cms_apps/admin_hp.html')


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
        log.info(kwargs)

        if kwargs['section']:
            data = self.serializer_class(site_config).data['values'][kwargs.get('section')]
            
        return Response(data)

    def update(self, request, *args, **kwargs):
        site_config = self.queryset.get(pk=kwargs.get('pk'))

        data = self.serializer_class(site_config).data['values']

        if kwargs['section']:
            data[kwargs.get('section')] = request.data
            log.info(data)

        serializer = self.serializer_class(site_config, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

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
