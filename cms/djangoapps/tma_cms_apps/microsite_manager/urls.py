from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    r'homepage',
    HomepageViewSet
)

router.register(
    r'faq',
    HomepageViewSet
)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/v1', include('rest_framework.urls', namespace='rest_framework'))
]