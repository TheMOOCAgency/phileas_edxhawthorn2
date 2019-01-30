from django.contrib import admin
from django.apps import apps
TmaCourseOverview = apps.get_model('tma_apps','TmaCourseOverview')
TmaCourseEnrollment = apps.get_model('tma_apps','TmaCourseEnrollment')

class TmaCourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course_id','user_edx','has_validated_course','completion_rate','is_favourite','is_liked','student_grade','best_student_grade','date_best_student_grade','has_displayed_message','enrollment_active')
    fields=('course_enrollment_edx','has_validated_course','completion_rate','is_favourite','is_liked','student_grade','best_student_grade','date_best_student_grade','has_displayed_message','enrollment_active')
    def user_edx(self, obj):
        return obj.course_enrollment_edx.user
    user_edx.admin_order_field = 'course_enrollment_edx'
    user_edx.short_description = 'User'
    def course_id(self, obj):
        return obj.course_enrollment_edx.course_id
    course_id.admin_order_field = 'course_enrollment_edx'
    course_id.short_description = 'Course ID'
    def enrollment_active(self, obj):
        return obj.course_enrollment_edx.is_active
    course_id.admin_order_field = 'course_enrollment_edx'
    course_id.short_description = 'Enrollment Active'

    readonly_fields =('course_enrollment_edx','enrollment_active')


class TmaCourseOverviewAdmin(admin.ModelAdmin):
    list_display = ('course_overview_edx','is_manager_only','is_mandatory','is_vodeclic','liked_total','favourite_total','is_course_graded','active_enrollments_total','tag')
    fields=('course_overview_edx','is_manager_only','is_mandatory','is_vodeclic','liked_total','favourite_total','is_course_graded','active_enrollments_total','tag')
    readonly_fields =('course_overview_edx',)

admin.site.register(TmaCourseEnrollment, TmaCourseEnrollmentAdmin)
admin.site.register(TmaCourseOverview, TmaCourseOverviewAdmin)
