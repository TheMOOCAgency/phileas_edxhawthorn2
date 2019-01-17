#!/usr/bin/env python
# -*- coding: utf-8 -*-
from student.models import CourseEnrollment
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from opaque_keys.edx.keys import CourseKey
from django.db import models
from django.dispatch import receiver
from student.signals import UNENROLL_DONE
import datetime
import logging
import json

log = logging.getLogger()

class TmaCourseEnrollment(models.Model):
    course_enrollment_edx = models.ForeignKey(
        CourseEnrollment,
        on_delete=models.CASCADE
        )
    course_time_tracking = models.IntegerField(default=0)
    detailed_time_tracking = models.TextField(blank=True)
    has_started_course = models.BooleanField(default=False)
    has_validated_course = models.BooleanField(default=False)
    is_favourite = models.BooleanField(default=False)
    completion_rate = models.FloatField(default=0)

    @classmethod
    def get_courseenrollment(cls, course_key, user):
        course_enrollment = CourseEnrollment.objects.get(course_id=course_key, user=user)
        enrollment, created = TmaCourseEnrollment.objects.get_or_create(
            course_enrollment_edx=course_enrollment,
        );
        return enrollment

    @classmethod
    def update_time_tracking(cls, course_key, user, course_time, section, sub_section):
        enrollment = cls.get_courseenrollment(course_key, user)
        try:
            if enrollment.detailed_time_tracking:
                detailed_time=json.loads(enrollment.detailed_time_tracking)
            else :
                detailed_time={}
            section_time = int(detailed_time.get(section,0))+ course_time
            sub_section_time = int(detailed_time.get(sub_section,0))+ course_time
            detailed_time[section]=section_time
            detailed_time[sub_section]=sub_section_time

            enrollment.course_time_tracking+=course_time
            enrollment.has_started_course=True
            enrollment.detailed_time_tracking=json.dumps(detailed_time)
            enrollment.save()
            return 'time tracking registration success'
        except:
            return 'error while registering time tracking'

    @classmethod
    def update_course_validation(cls, course_key, user, validation_status):
        enrollment = cls.get_courseenrollment(course_key, user)
        try :
            enrollment.has_validated_course=validation_status
            enrollment.save()
            return 'course validation status registration success'
        except:
            return 'error while registering course validation status'

    @classmethod
    def update_course_completion(cls, course_key, user, completion_rate):
        enrollment = cls.get_courseenrollment(course_key, user)
        try :
            enrollment.completion_rate=completion_rate
            enrollment.save()
            return 'course validation status registration success'
        except:
            return 'error while registering course validation status'

    @classmethod
    def update_favourite(cls, course_key, user, status):
        """
        Updates is_favorite attribute in TmaCourseEnrollment with status argument (bool)
        """

        response = {}
        if status is not None and isinstance(status, bool) :
            if TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=user, course_enrollment_edx__course_id=course_key).exists() :
                tma_enrollment = TmaCourseEnrollment.objects.get(course_enrollment_edx__user=user, course_enrollment_edx__course_id=course_key)
                tma_enrollment.is_favourite = status
                tma_enrollment.save()
            else :
                new_enrollment = CourseEnrollment.enroll(user, course_key, 'audit')
                new_enrollment.update_enrollment(is_active=False)
                TmaCourseEnrollment.objects.get_or_create(course_enrollment_edx=new_enrollment)[0].is_favourite = status
            response = {
                'success': 'Status updated',
                'status': status
            }
        else :
            response = {
                'error':_('Wrong parameters')
            }
        return response

    @classmethod
    def get_validated_courses(cls, user):
        validated_courses_nbr = 0
        validated_courses_nbr = TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=user, has_validated_course=True).count()
        return validated_courses_nbr

    @classmethod
    def get_ongoing_courses(cls, user):
        ongoing_courses_nbr = 0
        ongoing_courses_nbr = TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=user, completion_rate__gt=0).count()
        return ongoing_courses_nbr


#AUTO CREATE TmaCourseEnrollment when CourseEnrollment is created
@receiver(models.signals.post_save, sender=CourseEnrollment)
def create_tmacourseenrollement(sender, instance, **kwargs):
    if kwargs['created']:
        TmaCourseEnrollment.objects.get_or_create(
            course_enrollment_edx=instance,
        );



############################## TMA COURSE OVERVIEW ################################################################

class TmaCourseOverview(models.Model):
    course_overview_edx = models.ForeignKey(CourseOverview)
    is_manager_only = models.BooleanField(default=False)
    is_mandatory = models.BooleanField(default=False)
    is_vodeclic = models.BooleanField(default=False)

    @classmethod
    def get_course_overview(cls, course_key, user):
        course_overview = CourseOverview.objects.get(course_id=course_key)
        tma_course_overview, created = TmaCourseOverview.objects.get_or_create(
            course_enrollment_edx=course_overview,
        );
        return tma_course_overview