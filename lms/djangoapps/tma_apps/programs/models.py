#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from student.models import CourseEnrollment
from django.contrib.auth.models import User
import logging
import datetime 

log = logging.getLogger()

class TmaProgramEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(default=datetime.now())
    has_started_program = models.BooleanField(default=False)
    has_validated_program = models.BooleanField(default=False)
    program_completion_rate = models.FloatField(default=0)

class TmaProgramOverview(models.Model):
    is_manager_only = models.BooleanField(default=False)
    is_mandatory = models.BooleanField(default=False)
    is_linear = models.BooleanField(default=False)
    invitation_only = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    program_start_date = models.DateTimeField(null=True)
    program_due_date = models.DateTimeField(null=True)

class TmaProgramCourse(models.Model):
    program = models.ForeignKey(TmaProgramEnrollment, on_delete=models.CASCADE, unique=True)
    course = models.ForeignKey(CourseEnrollment, on_delete=models.CASCADE, unique=True)
    order = models.IntegerField(default=0)
