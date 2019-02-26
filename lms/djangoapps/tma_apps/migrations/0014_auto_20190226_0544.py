# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-26 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tma_apps', '0013_auto_20190201_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmacourseoverview',
            name='course_about',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='tmacourseoverview',
            name='tag',
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
    ]
