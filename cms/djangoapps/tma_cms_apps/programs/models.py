# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User


class TmaProgramOverview(models.Model):
    is_manager_only = models.BooleanField(default=False)
    is_mandatory = models.BooleanField(default=False)
    is_linear = models.BooleanField(default=False)
    invitation_only = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    program_start_date = models.DateTimeField(db_index=True, null=True)
    program_due_date = models.DateTimeField(db_index=True, null=True)
    program_name = models.CharField(default='program name',max_length=50)

class TmaProgramCourse(models.Model):
    program = models.ForeignKey(TmaProgramOverview, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseOverview, on_delete=models.CASCADE, unique=True)
    order = models.IntegerField(default=0)
