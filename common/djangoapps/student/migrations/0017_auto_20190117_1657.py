# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-17 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_coursenrollment_course_on_delete_do_nothing'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_manager',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='iug',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rpid',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
