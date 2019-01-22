# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-18 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tma_apps', '0003_tmacourseenrollment_is_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmacourseenrollment',
            name='best_student_grade',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='tmacourseenrollment',
            name='date_best_student_grade',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
