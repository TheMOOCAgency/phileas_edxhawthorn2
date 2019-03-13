#!/usr/bin/env python

import os
import importlib
from django.core.management import execute_from_command_line
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.envs.aws")
os.environ.setdefault("lms.envs.aws,SERVICE_VARIANT", "cms")
os.environ.setdefault("PATH", "/edx/app/edxapp/venvs/edxapp/bin:/edx/app/edxapp/edx-platform/bin:/edx/app/edxapp/.rbenv/bin:/edx/app/edxapp/.rbenv/shims:/edx/app/edxapp/.gem/bin:/edx/app/edxapp/edx-platform/node_modules/.bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin")
os.environ.setdefault("SERVICE_VARIANT", "cms")
os.chdir("/edx/app/edxapp/edx-platform")
startup = importlib.import_module("cms.startup")
startup.run()

from tma_cms_apps.vodeclic_generate_courses.generate_courses import VodeclicGenerator

#Be sure to get all course pictures
VodeclicGenerator().save_all_courses_pictures('fr')
VodeclicGenerator().save_all_courses_pictures('en')

#Ids of courses to create
courses_id_fr=["223","2005","2555","2353","98","2423","2911","3123","915","517","797","3153","1415","2087","209","194","3181","1909","791","2577","1085","747","2681","2925","3077","991","691","377","677","1049","735","3175","375","192","2559","347","210","1667","200","1649","689","222","196","1601","1149","1785","217","2787","757","383","2291","3163","2097","2225","2093","2179","591","212","1677","1155","3065","1407","346","190","2921","755"]

courses_id_en=["431","2023","1645","2355","2639","2991","3125","2625","1091","1933","3161","2273","1529","2089","232","1671","2431","3187","887","2723","1919","983","1783","2731","492","2975","2927","1009","1631","743","3177","2665","2485","1837","428","1817","2449","2275","234","1673","2365","1741","233","1629","2337","867","2111","1743","1787","435","2917","2479","2315","2293","2335","3165","2583","2099","2227","3031","2209","430","1679","3131","1511","348","235","1637","2411"]

organizations=('europe', 'asia', 'americas')

#Launches course creation for each language
for organization in organizations :
    VodeclicGenerator().update_vodeclic_courses(courses_id_fr, organization, 'fr')
    VodeclicGenerator().update_vodeclic_courses(courses_id_en, organization, 'en')
