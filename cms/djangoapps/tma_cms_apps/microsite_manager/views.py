from rest_framework import viewsets

from openedx.core.djangoapps.site_configuration.models import SiteConfiguration


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class HomepageViewSet(viewsets.ModelViewSet):
    queryset = SiteConfiguration.objects.all()
    #serializer_class = UserSerializer

class FaqViewSet(viewsets.ModelViewSet):
    # Where is stored FAQ ?