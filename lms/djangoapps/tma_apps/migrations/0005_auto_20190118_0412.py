# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-18 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tma_apps', '0004_auto_20190118_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmacourseoverview',
            name='favourite_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tmacourseoverview',
            name='liked_total',
            field=models.IntegerField(default=0),
        ),
    ]
