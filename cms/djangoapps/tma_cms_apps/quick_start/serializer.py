import logging
log = logging.getLogger()

from rest_framework import serializers
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from lms.djangoapps.courseware.courses import get_course_by_id
from lms.djangoapps.tma_apps.models import TmaCourseOverview
from tma_cms_apps.quick_start.helpers import TmaCourseCreator


class CourseSerializer(serializers.Serializer):
    course_name = serializers.CharField(required=True)
    course_number = serializers.CharField(required=True)
    course_session = serializers.CharField(required=True)
    org = serializers.CharField(required=True)
    language = serializers.CharField(required=True)
    short_description = serializers.CharField(required=True)
    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)
    effort = serializers.IntegerField(required=True)
    is_course_graded=serializers.BooleanField(required=True)
    is_manager_only=serializers.BooleanField(required=True)
    is_mandatory=serializers.BooleanField(required=True)
    has_menu=serializers.BooleanField(required=True)
    is_course_graded=serializers.BooleanField(required=True)
    tag=serializers.CharField(required=True)
    onboarding=serializers.CharField(required=True)


    def validate (self, data):
        """
        Check validity of argument to create course
        """
        course_key=SlashSeparatedCourseKey.from_deprecated_string('course-v1:'+data['org']+'+'+data['course_number']+'+'+data['course_session'])
        try :
            course=get_course_by_id(course_key)
        except:
            course=None
        if course :
            raise serializers.ValidationError("course_id already exists")
        if TmaCourseOverview.objects.filter(course_overview_edx=course_key).exists():
            raise serializers.ValidationError("TmaCourseOverview already exists")
        return data
    
    def create(self, validated_data):
        """
        Launch course creation
        """
        return TmaCourseCreator().createCourse(validated_data)    

