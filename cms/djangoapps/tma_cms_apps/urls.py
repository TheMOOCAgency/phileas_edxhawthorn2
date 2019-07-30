from django.conf.urls import include, url
from rest_framework import routers

from cms.djangoapps.tma_cms_apps.microsite_manager import views

import logging
log = logging.getLogger(__name__)

router = routers.DefaultRouter()

router.register(
    r'^microsite_manager/$',
    views.SiteConfigurationDetailViewSet,
    base_name='site-configuration-detail'
)

urlpatterns = [
    # UI Templates
    url(r'^manager/pages/homepage/(?P<id>.+)/$', views.admin_homepage, name='admin-homepage'),

    url(r'^api/v1/$', include(router.urls, namespace='api')),
    url(
        r'^api/v1/microsite_manager/(?P<pk>[0-9]+)/(?P<section>.+)/$',
        views.SiteConfigurationAPIView.as_view(),
        name='site-configuration'
    )
]