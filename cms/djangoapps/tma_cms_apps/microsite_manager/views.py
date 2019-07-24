import json
import logging

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response

from openedx.core.djangoapps.site_configuration.models import SiteConfiguration

log = logging.getLogger(__name__)


class SiteConfigurationSerializer(serializers.ModelSerializer):
    values = serializers.JSONField()    

    class Meta:
        model = SiteConfiguration
        fields = ['values']

    def get_values(self, obj):
        log.info(dict(obj.values))
        log.info(type(obj.values))
        return json.dumps(obj.values)


class HomepageDetailViewSet(viewsets.ViewSet):
    '''
    Returns homepage content information for requested microsite.
    '''
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]
    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigurationSerializer

    def retrieve(self, request, pk=None):
        site_config = get_object_or_404(self.queryset, pk=pk)
        data = SiteConfigurationSerializer(site_config).data

        return Response(data['values'])

    def partial_update(self, request):
        site_config = self.queryset.get(pk=kwargs.get('pk'))
        previous_data = site_config.data
        new_data = update(previous_data,champ,valeur)
        serializer = self.serializer_class(site_config, data=new_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)