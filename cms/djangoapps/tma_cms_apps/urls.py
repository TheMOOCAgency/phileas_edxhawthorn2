from django.conf.urls import include, url
from rest_framework import routers

from cms.djangoapps.tma_cms_apps.microsite_manager import views

import logging
log = logging.getLogger(__name__)

router = routers.DefaultRouter()

router.register(
    r'microsite_manager',
    views.HomepageDetailViewSet,
    base_name='homepage-detail'
)

urlpatterns = [
    url(r'^api/v1/', include(router.urls, namespace='api')),
]