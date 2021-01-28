# -*- coding: utf-8 -*-
import sys
import csv
import os
import json
import logging
import importlib

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lms.envs.aws")
os.environ.setdefault("lms.envs.aws,SERVICE_VARIANT", "lms")
os.environ.setdefault("PATH", "/edx/app/edxapp/venvs/edxapp/bin:/edx/app/edxapp/edx-platform/bin:/edx/app/edxapp/.rbenv/bin:/edx/app/edxapp/.rbenv/shims:/edx/app/edxapp/.gem/bin:/edx/app/edxapp/edx-platform/node_modules/.bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin")

os.environ.setdefault("SERVICE_VARIANT", "lms")
os.chdir("/edx/app/edxapp/edx-platform")

startup = importlib.import_module("lms.startup")
startup.run()

from django.contrib.auth.models import User
from student.models import UserProfile, CourseEnrollmentAllowed
log = logging.getLogger()

def update_amundi_email(user):
    user.email = user.email.replace("@amundipioneer.com", "@amundi.com")
    user.save(update_fields=['email'])

amundi_users = User.objects.filter(email__contains="@amundipioneer.com")
map(update_amundi_email, amundi_users)