# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-29 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tma_apps', '0009_tmacourseenrollment_has_displayed_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmacourseoverview',
            name='active_enrollments_total',
            field=models.IntegerField(default=0),
        ),
    ]
