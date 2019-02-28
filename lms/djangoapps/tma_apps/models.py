#!/usr/bin/env python
# -*- coding: utf-8 -*-
from student.models import CourseEnrollment
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from opaque_keys.edx.keys import CourseKey
from django.db import models
from django.dispatch import receiver
from student.signals import UNENROLL_DONE
from student.signals import ENROLL_STATUS_CHANGE
import datetime
import collections
import logging
import json
from jsonfield.fields import JSONField
from django.utils.translation import ugettext as _
log = logging.getLogger()

class TmaCourseEnrollment(models.Model):
    course_enrollment_edx = models.ForeignKey(
        CourseEnrollment,
        on_delete=models.CASCADE,
        unique=True
        )
    course_time_tracking = models.IntegerField(default=0)
    detailed_time_tracking = models.TextField(blank=True)
    has_started_course = models.BooleanField(default=False)
    has_validated_course = models.BooleanField(default=False)
    is_favourite = models.BooleanField(default=False)
    is_liked = models.BooleanField(default=False)
    has_displayed_message = models.BooleanField(default=False)
    completion_rate = models.FloatField(default=0)
    quiz_completion_rate = models.FloatField(default=0)
    student_grade = models.FloatField(default=0)
    best_student_grade = models.FloatField(default=0)
    date_best_student_grade = models.DateTimeField(blank=True,null=True)

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
    def update_course_completion(cls, course_key, user, completion_rate, quiz_completion_rate):
        enrollment = cls.get_courseenrollment(course_key, user)
        try :
            enrollment.completion_rate=completion_rate
            enrollment.quiz_completion_rate=quiz_completion_rate
            enrollment.save()
            return 'course validation status registration success'
        except:
            return 'error while registering course validation status'


    @classmethod
    def update_grade(cls,course_key,user,grade,passed):
        response={}
        enrollment = cls.get_courseenrollment(course_key,user)
        try :
            response['new_best_grade']=False
            response['success_moment']=False
            enrollment.student_grade=grade
            if grade > enrollment.best_student_grade:
                enrollment.best_student_grade = grade
                enrollment.date_best_student_grade = datetime.datetime.now()
                response['new_best_grade']=True
            enrollment.has_validated_course = passed
            enrollment.save()
            response['status']='success'
            response['has_displayed_message']=enrollment.has_displayed_message
        except:
            response['status']='error'
        return response


    @classmethod
    def update_social_attributes(cls,attribute,course_key,user,status):
        """
        Update is_liked and is_favourite + create CourseEnrollmentEdx if doesn't exists
        """
        response = {}
        if status is not None and attribute is not None and isinstance(status, bool) :
            if not CourseEnrollment.objects.filter(course_id=course_key, user=user).exists():
                edx_enrollment = CourseEnrollment.enroll(user, course_key, 'audit')
                edx_enrollment.update_enrollment(is_active=False)
            tma_enrollment = cls.get_courseenrollment(course_key,user)
            if attribute=="is_favourite":
                tma_course_overview = TmaCourseOverview.get_tma_course_overview_by_course_id(course_key)
                if status and (tma_enrollment.is_favourite != status):
                    tma_course_overview.favourite_total += 1
                elif not status and (tma_enrollment.is_favourite != status):
                    tma_course_overview.favourite_total -= 1
                tma_enrollment.is_favourite=status
            elif attribute=="is_liked":
                tma_course_overview = TmaCourseOverview.get_tma_course_overview_by_course_id(course_key)
                if status and (tma_enrollment.is_liked != status):
                    tma_course_overview.liked_total += 1
                elif not status and (tma_enrollment.is_liked != status):
                    tma_course_overview.liked_total -= 1
                tma_enrollment.is_liked=status
            tma_course_overview.save()
            tma_enrollment.save()
            response = {
                'success': attribute+' status updated ',
                'status': status
            }
        else :
            response = {
                'error':_('Wrong parameters')
            }
        return response


    @classmethod
    def get_validated_courses(cls, user, org):
        validated_courses_nbr = 0
        validated_courses_nbr = TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=user,course_enrollment_edx__course__org=org, has_validated_course=True).count()
        return validated_courses_nbr

    @classmethod
    def count_ongoing_courses(cls, user, org):
        ongoing_courses = TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=user,course_enrollment_edx__course__org=org, has_validated_course=False,course_enrollment_edx__is_active=True).count()
        return ongoing_courses

    @classmethod
    def count_favorite_courses(cls, user, org):
        favorite_courses = TmaCourseEnrollment.objects.filter(course_enrollment_edx__user=user,course_enrollment_edx__course__org=org, is_favourite=True).count()
        return favorite_courses

#AUTO CREATE TmaCourseEnrollment when CourseEnrollment is created
@receiver(models.signals.post_save, sender=CourseEnrollment)
def create_tmacourseenrollement(sender, instance, **kwargs):
    if kwargs['created']:
        TmaCourseEnrollment.objects.get_or_create(
            course_enrollment_edx=instance,
        );



############################## TMA COURSE OVERVIEW ################################################################

class TmaCourseOverview(models.Model):
    course_overview_edx = models.ForeignKey(CourseOverview, unique=True)
    is_manager_only = models.BooleanField(default=False)
    is_mandatory = models.BooleanField(default=False)
    is_vodeclic = models.BooleanField(default=False)
    favourite_total = models.IntegerField(default=0)
    liked_total = models.IntegerField(default=0)
    active_enrollments_total = models.IntegerField(default=0)
    is_course_graded = models.BooleanField(default=True)
    tag = models.CharField(db_index=True, max_length=50, default=False)
    course_about = JSONField(null=False, default=collections.OrderedDict, load_kwargs={'object_pairs_hook': collections.OrderedDict})

    @classmethod
    def get_tma_course_overview_by_course_id(cls, course_key):
        try:
            course_overview = CourseOverview.objects.get(id=course_key)
            tma_course_overview, created = TmaCourseOverview.objects.get_or_create(
                course_overview_edx=course_overview,
            );
            return tma_course_overview
        except:
            pass

    @classmethod
    def add_vodelic_course(cls, course_key):
        tma_course_overview=cls.get_tma_course_overview_by_course_id(course_key)
        tma_course_overview.is_vodeclic=True
        tma_course_overview.save()
        return tma_course_overview

    @classmethod
    def change_active_enrollments_total(cls, course_key, event):
        tma_course_overview=cls.get_tma_course_overview_by_course_id(course_key)
        if event=="enroll":
            tma_course_overview.active_enrollments_total+=1
        elif event=="unenroll":
            tma_course_overview.active_enrollments_total-=1
        tma_course_overview.save()
        return tma_course_overview

    @classmethod
    def count_mandatory_courses(cls, org):
        mandatory_courses = TmaCourseOverview.objects.filter(course_overview_edx__org=org, is_mandatory=True).count()
        return mandatory_courses

    @classmethod
    def get_all_tags(cls, org):
        all_tags = []
        try:
            tag_lists = TmaCourseOverview.objects.filter(course_overview_edx__org=org).values_list('tag', flat=True)
            for tag in tag_lists:
                if ',' in str(tag):
                    all_tags.extend(tag.split(','))
                else:
                    all_tags.append(str(tag))

            all_tags = collections.Counter(all_tags)
        except:
            pass
        
        return all_tags

#Track enrollments and unenrollments to update total_active_enrollments
@receiver(ENROLL_STATUS_CHANGE)
def update_active_enrollments_total(sender, event=None, user=None, **kwargs):
    TmaCourseOverview.change_active_enrollments_total(kwargs['course_id'], event)