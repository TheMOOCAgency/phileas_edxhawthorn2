from django.contrib import admin
from django.apps import apps
TmaCourseOverview = apps.get_model('tma_apps','TmaCourseOverview')
TmaCourseEnrollment = apps.get_model('tma_apps','TmaCourseEnrollment')

class TmaCourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course_id','user_edx','has_validated_course','completion_rate','is_favourite','is_liked','student_grade','best_student_grade','date_best_student_grade')
    fields=('course_enrollment_edx','has_validated_course','completion_rate','is_favourite','is_liked','student_grade','best_student_grade','date_best_student_grade')
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
    list_display = ('course_overview_edx','is_manager_only','is_mandatory','is_vodeclic','liked_total','favourite_total')
    fields=('course_overview_edx','is_manager_only','is_mandatory','is_vodeclic','liked_total','favourite_total')
    readonly_fields =('course_overview_edx',)

admin.site.register(TmaCourseEnrollment, TmaCourseEnrollmentAdmin)
admin.site.register(TmaCourseOverview, TmaCourseOverviewAdmin)
