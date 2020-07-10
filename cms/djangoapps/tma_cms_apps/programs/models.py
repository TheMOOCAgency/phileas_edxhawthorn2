# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
import logging

log = logging.getLogger()

class TmaProgramOverview(models.Model):
    is_manager_only = models.BooleanField(default=False)
    is_mandatory = models.BooleanField(default=False)
    is_linear = models.BooleanField(default=False)
    invitation_only = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    program_start_date = models.DateTimeField(db_index=True, auto_now_add=True, null=True)
    program_due_date = models.DateTimeField(db_index=True, auto_now_add=True, null=True)
    program_name = models.CharField(default='program name',max_length=50)

class TmaProgramEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(TmaProgramOverview, on_delete=models.CASCADE, unique=True)
    enrollment_date = models.DateTimeField(db_index=True, auto_now_add=True, null=True)
    has_started_program = models.BooleanField(default=False)
    has_validated_program = models.BooleanField(default=False)
    program_completion_rate = models.FloatField(default=0)

class TmaProgramCourse(models.Model):
    program = models.ForeignKey(TmaProgramEnrollment, on_delete=models.CASCADE, unique=True)
    course = models.ForeignKey(CourseOverview, on_delete=models.CASCADE, unique=True)
    order = models.IntegerField(default=0)
