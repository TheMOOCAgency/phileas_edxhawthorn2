from django.contrib import admin
from tma_apps.models import TmaCourseEnrollment, TmaCourseOverview

class TmaCourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course_id','user_edx','has_validated_course','completion_rate','is_favourite',)
    fields=('course_enrollment_edx','has_validated_course','completion_rate','is_favourite',)
    def user_edx(self, obj):
        return obj.course_enrollment_edx.user
    user_edx.admin_order_field = 'course_enrollment_edx'
    user_edx.short_description = 'User'
    def course_id(self, obj):
        return obj.course_enrollment_edx.course_id
    course_id.admin_order_field = 'course_enrollment_edx'
    course_id.short_description = 'Course ID'

    readonly_fields =('course_enrollment_edx',)


class TmaCourseOverviewAdmin(admin.ModelAdmin):
    list_display = ('course_id','user_edx','is_manager_only','is_mandatory','is_vodeclic',)
    fields=('course_overview_edx','is_manager_only','is_mandatory','is_vodeclic',)
    def user_edx(self, obj):
        return obj.course_overview_edx.user
    user_edx.admin_order_field = 'course_overview_edx'
    user_edx.short_description = 'User'
    def course_id(self, obj):
        return obj.course_overview_edx.course_id
    course_id.admin_order_field = 'course_overview_edx'
    course_id.short_description = 'Course ID'



admin.site.register(TmaCourseEnrollment, TmaCourseEnrollmentAdmin)
admin.site.register(TmaCourseOverview, TmaCourseOverviewAdmin)
