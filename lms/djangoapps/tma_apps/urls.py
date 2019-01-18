from django.conf.urls import url
from django.conf import settings
from .certificates import views as certificates_views
from .grade_tracking import views as grade_views
from .completion import views as completion_views
from .favourite import views as favourite_views
from .activity_dashboard import views as activity_dashboard_views


urlpatterns = [
    #Certificates
    url(r'^{}/certificate/ensure$'.format(settings.COURSE_ID_PATTERN), certificates_views.ensure),
    url(r'^{}/certificate/render$'.format(settings.COURSE_ID_PATTERN), certificates_views.render),

    #Completion
    url(r'^{}/completion/get_course_completion$'.format(settings.COURSE_ID_PATTERN), completion_views.get_course_completion),


    #Favoris
    url(r'^{}/favourite/update_favourite$'.format(settings.COURSE_ID_PATTERN), favourite_views.api_update_favourite),

    #Liked
    url(r'^{}/liked/update_liked$'.format(settings.COURSE_ID_PATTERN), favourite_views.api_update_favourite),

    # Home dashboard
    url(r'^dashboard/home/$', activity_dashboard_views.home_dashboard, name='home_dashboard'),

    #Student Grade Tracking
    url(r'^{}/grade_tracking/get_user_grade$'.format(settings.COURSE_ID_PATTERN), grade_views.get_user_grade),
]
