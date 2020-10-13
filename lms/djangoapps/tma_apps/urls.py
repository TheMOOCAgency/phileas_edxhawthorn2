from django.conf.urls import url
from django.conf import settings
from .certificates import views as certificates_views
from .grade_tracking import views as grade_views
from .completion import views as completion_views
from .favourite import views as favourite_views
from .like import views as like_views
from .activity_dashboard import views as activity_dashboard_views
from .delete_cookies import views as delete_cookies_views
from .legal import views as legal_views
from .tma_reports import views as tma_reports_views
from .average_score import views as average_views
from .faq import views as faq_views
from .new_dashboard import views as new_dashboard_views

urlpatterns = [
    #Certificates
    url(r'^{}/certificate/ensure$'.format(settings.COURSE_ID_PATTERN), certificates_views.ensure),
    url(r'^{}/certificate/render$'.format(settings.COURSE_ID_PATTERN), certificates_views.render),
    url(r'^{}/certificate/check_best_grade$'.format(settings.COURSE_ID_PATTERN), certificates_views.check_best_grade),
    url(r'^{}/certificate/generate$'.format(settings.COURSE_ID_PATTERN), certificates_views.generate),

    #Completion
    url(r'^{}/completion/get_course_completion$'.format(settings.COURSE_ID_PATTERN), completion_views.get_course_completion),
    url(r'^{course_id}/{unit_id}/completion/get_unit_completion$'.format(course_id=settings.COURSE_ID_PATTERN, unit_id=settings.USAGE_KEY_PATTERN), completion_views.get_unit_completion),

    #Favoris
    url(r'^{}/favorite/update_favorite$'.format(settings.COURSE_ID_PATTERN), favourite_views.api_update_favourite),

    #Liked
    url(r'^{}/like/update_like$'.format(settings.COURSE_ID_PATTERN), like_views.api_update_like),

    # Courses dashboard
    url(r'^dashboard/home/courses$', activity_dashboard_views.home_dashboard_courses, name='home_dashboard_courses'),

    # Programs dashboard
    url(r'^dashboard/home/programs$', activity_dashboard_views.programs_dashboard_view, name='programs_dashboard_view'),

    #Student Grade Tracking
    url(r'^{}/grade_tracking/get_user_grade$'.format(settings.COURSE_ID_PATTERN), grade_views.get_user_grade),
    url(r'^{}/grade_tracking/message_displayed$'.format(settings.COURSE_ID_PATTERN), grade_views.mark_displayed_message),
    url(r'^{}/grade_tracking/mark_as_done$'.format(settings.COURSE_ID_PATTERN), grade_views.mark_as_done),
    url(r'^{}/grade_tracking/try_again$'.format(settings.COURSE_ID_PATTERN), grade_views.try_again),

    #Logout
    url(r'^delete_cookies$', delete_cookies_views.tma_delete_cookies),

    # Legal
    url(r'^legal$', legal_views.legal_notice_page),

    #TTMA specific reports
    url(r'^{}/export_invited$'.format(settings.COURSE_ID_PATTERN), tma_reports_views.download_invited_report, name="export_invited"),

    # TMA average grade page
    url(
        r'^{}/progress/average$'.format(
            settings.COURSE_ID_PATTERN,
        ),
        average_views.average,
        name='average',
    ),

    #TMA faq
    url(r'^faq$', faq_views.faq_view),

    # New Dashboard
    url(r'^view_enrollments$', new_dashboard_views.view_enrollments),
    url(r'^new_tma_dashboard$', new_dashboard_views.new_tma_dashboard_view),
]
