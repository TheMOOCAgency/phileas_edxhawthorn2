# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-16 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_overviews', '0014_courseoverview_certificate_available_date'),
        ('student', '0016_coursenrollment_course_on_delete_do_nothing'),
    ]

    operations = [
        migrations.CreateModel(
            name='TmaCourseEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_time_tracking', models.IntegerField(default=0)),
                ('detailed_time_tracking', models.TextField(blank=True)),
                ('has_started_course', models.BooleanField(default=False)),
                ('has_validated_course', models.BooleanField(default=False)),
                ('is_favourite', models.BooleanField(default=False)),
                ('completion_rate', models.FloatField(default=0)),
                ('course_enrollment_edx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.CourseEnrollment')),
            ],
        ),
        migrations.CreateModel(
            name='TmaCourseOverview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_manager_only', models.BooleanField(default=False)),
                ('is_mandatory', models.BooleanField(default=False)),
                ('is_vodeclic', models.BooleanField(default=False)),
                ('course_overview_edx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_overviews.CourseOverview')),
            ],
        ),
    ]