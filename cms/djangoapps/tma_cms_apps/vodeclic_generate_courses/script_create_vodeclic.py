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
#VodeclicGenerator().save_all_courses_pictures('fr')
#VodeclicGenerator().save_all_courses_pictures('en')

#Ids of courses to create
courses_id_fr={
"1049":{"tags":"Communication","pictos":"Megaphone"},
"1085":{"tags":"Business App.","pictos":"Cartable"},
"1149":{"tags":"Design","pictos":"Pencil"},
"1155":{"tags":"Communication","pictos":"Megaphone"},
"1407":{"tags":"Internet","pictos":"MapMonde"},
"1415":{"tags":"Internet","pictos":"MapMonde"},
"1601":{"tags":"Office Tools","pictos":"Computer"},
"1649":{"tags":"Communication","pictos":"Megaphone"},
"1667":{"tags":"Office Tools","pictos":"Computer"},
"1677":{"tags":"Business App.","pictos":"Cartable"},
"1785":{"tags":"Business App.","pictos":"Cartable"},
"190":{"tags":"Office Tools","pictos":"Computer"},
"1909":{"tags":"Communication","pictos":"Megaphone"},
"192":{"tags":"Office Tools","pictos":"Computer"},
"194":{"tags":"Office Tools","pictos":"Computer"},
"196":{"tags":"Office Tools","pictos":"Computer"},
"200":{"tags":"Communication","pictos":"Megaphone"},
"2005":{"tags":"Office Tools","pictos":"Computer"},
"2087":{"tags":"Office Tools","pictos":"Computer"},
"209":{"tags":"Office Tools","pictos":"Computer"},
"2093":{"tags":"Communication","pictos":"Megaphone"},
"2097":{"tags":"Business App.","pictos":"Cartable"},
"210":{"tags":"Office Tools","pictos":"Computer"},
"212":{"tags":"Business App.","pictos":"Cartable"},
"217":{"tags":"Office Tools","pictos":"Computer"},
"2179":{"tags":"Communication","pictos":"Megaphone"},
"222":{"tags":"Design","pictos":"Pencil"},
"2225":{"tags":"Business App.","pictos":"Cartable"},
"223":{"tags":"Office Tools","pictos":"Computer"},
"2291":{"tags":"Business App.","pictos":"Cartable"},
"2353":{"tags":"Communication","pictos":"Megaphone"},
"2423":{"tags":"Internet","pictos":"MapMonde"},
"2555":{"tags":"Office Tools","pictos":"Computer"},
"2555":{"tags":"Office Tools","pictos":"Computer"},
"2559":{"tags":"Communication","pictos":"Megaphone"},
"2577":{"tags":"Communication","pictos":"Megaphone"},
"2681":{"tags":"Communication","pictos":"Megaphone"},
"2787":{"tags":"Office Tools","pictos":"Computer"},
"2911":{"tags":"Internet","pictos":"MapMonde"},
"2921":{"tags":"Communication","pictos":"Megaphone"},
"2925":{"tags":"Internet","pictos":"MapMonde"},
"3065":{"tags":"Communication","pictos":"Megaphone"},
"3077":{"tags":"Internet","pictos":"MapMonde"},
"3123":{"tags":"Business App.","pictos":"Cartable"},
"3153":{"tags":"Business App.","pictos":"Cartable"},
"3163":{"tags":"Design","pictos":"Pencil"},
"3175":{"tags":"Internet","pictos":"MapMonde"},
"3181":{"tags":"Office Tools","pictos":"Computer"},
"346":{"tags":"Internet","pictos":"MapMonde"},
"347":{"tags":"Internet","pictos":"MapMonde"},
"375":{"tags":"Design","pictos":"Pencil"},
"377":{"tags":"Design","pictos":"Pencil"},
"383":{"tags":"Business App.","pictos":"Cartable"},
"517":{"tags":"Internet","pictos":"MapMonde"},
"591":{"tags":"Communication","pictos":"Megaphone"},
"677":{"tags":"Design","pictos":"Pencil"},
"689":{"tags":"Design","pictos":"Pencil"},
"691":{"tags":"Design","pictos":"Pencil"},
"735":{"tags":"Internet","pictos":"MapMonde"},
"747":{"tags":"Design","pictos":"Pencil"},
"755":{"tags":"Communication","pictos":"Megaphone"},
"757":{"tags":"Design","pictos":"Pencil"},
"791":{"tags":"Communication","pictos":"Megaphone"},
"797":{"tags":"Communication","pictos":"Megaphone"},
"915":{"tags":"Design","pictos":"Pencil"},
"98":{"tags":"Office Tools","pictos":"Computer"},
"991":{"tags":"Communication","pictos":"Megaphone"},
}

courses_id_en={
"1009":{"tags":"Communication","pictos":"Megaphone"},
"1091":{"tags":"Communication","pictos":"Megaphone"},
"1511":{"tags":"Internet","pictos":"MapMonde"},
"1529":{"tags":"Internet","pictos":"MapMonde"},
"1629":{"tags":"Office Tools","pictos":"Computer"},
"1631":{"tags":"Communication","pictos":"Megaphone"},
"1637":{"tags":"Office Tools","pictos":"Computer"},
"1645":{"tags":"Office Tools","pictos":"Computer"},
"1645":{"tags":"Office Tools","pictos":"Computer"},
"1671":{"tags":"Office Tools","pictos":"Computer"},
"1673":{"tags":"Communication","pictos":"Megaphone"},
"1679":{"tags":"Business App.","pictos":"Cartable"},
"1741":{"tags":"Design","pictos":"Pencil"},
"1743":{"tags":"Design","pictos":"Pencil"},
"1783":{"tags":"Business App.","pictos":"Cartable"},
"1787":{"tags":"Business App.","pictos":"Cartable"},
"1817":{"tags":"Office Tools","pictos":"Computer"},
"1837":{"tags":"Business App.","pictos":"Cartable"},
"1919":{"tags":"Communication","pictos":"Megaphone"},
"1933":{"tags":"Design","pictos":"Pencil"},
"2015":{"tags":"Communication","pictos":"Megaphone"},
"2023":{"tags":"Office Tools","pictos":"Computer"},
"2089":{"tags":"Office Tools","pictos":"Computer"},
"2099":{"tags":"Business App.","pictos":"Cartable"},
"2111":{"tags":"Design","pictos":"Pencil"},
"2209":{"tags":"Communication","pictos":"Megaphone"},
"2227":{"tags":"Business App.","pictos":"Cartable"},
"2273":{"tags":"Business App.","pictos":"Cartable"},
"2275":{"tags":"Office Tools","pictos":"Computer"},
"2293":{"tags":"Business App.","pictos":"Cartable"},
"2315":{"tags":"Communication","pictos":"Megaphone"},
"232":{"tags":"Office Tools","pictos":"Computer"},
"233":{"tags":"Office Tools","pictos":"Computer"},
"2335":{"tags":"Business App.","pictos":"Cartable"},
"2337":{"tags":"Office Tools","pictos":"Computer"},
"234":{"tags":"Communication","pictos":"Megaphone"},
"235":{"tags":"Office Tools","pictos":"Computer"},
"2355":{"tags":"Communication","pictos":"Megaphone"},
"2365":{"tags":"Communication","pictos":"Megaphone"},
"2411":{"tags":"Office Tools","pictos":"Computer"},
"2431":{"tags":"Office Tools","pictos":"Computer"},
"2449":{"tags":"Office Tools","pictos":"Computer"},
"2479":{"tags":"Internet","pictos":"MapMonde"},
"2485":{"tags":"Internet","pictos":"MapMonde"},
"2583":{"tags":"Communication","pictos":"Megaphone"},
"2625":{"tags":"Business App.","pictos":"Cartable"},
"2639":{"tags":"Internet","pictos":"MapMonde"},
"2665":{"tags":"Communication","pictos":"Megaphone"},
"2723":{"tags":"Office Tools","pictos":"Computer"},
"2731":{"tags":"Communication","pictos":"Megaphone"},
"2917":{"tags":"Office Tools","pictos":"Computer"},
"2927":{"tags":"Internet","pictos":"MapMonde"},
"2975":{"tags":"Internet","pictos":"MapMonde"},
"2991":{"tags":"Internet","pictos":"MapMonde"},
"3031":{"tags":"Communication","pictos":"Megaphone"},
"3125":{"tags":"Business App.","pictos":"Cartable"},
"3131":{"tags":"Communication","pictos":"Megaphone"},
"3161":{"tags":"Business App.","pictos":"Cartable"},
"3165":{"tags":"Design","pictos":"Pencil"},
"3177":{"tags":"Internet","pictos":"MapMonde"},
"3187":{"tags":"Office Tools","pictos":"Computer"},
"348":{"tags":"Internet","pictos":"MapMonde"},
"428":{"tags":"Office Tools","pictos":"Computer"},
"430":{"tags":"Business App.","pictos":"Cartable"},
"431":{"tags":"Office Tools","pictos":"Computer"},
"435":{"tags":"Office Tools","pictos":"Computer"},
"492":{"tags":"Internet","pictos":"MapMonde"},
"743":{"tags":"Internet","pictos":"MapMonde"},
"867":{"tags":"Office Tools","pictos":"Computer"},
"875":{"tags":"Office Tools","pictos":"Computer"},
"887":{"tags":"Office Tools","pictos":"Computer"},
"983":{"tags":"Communication","pictos":"Megaphone"},
}


organizations=('europe', 'asia', 'americas')

#Launches course creation for each language
for organization in organizations :
    VodeclicGenerator().update_vodeclic_courses(courses_id_fr, organization, 'fr')
    VodeclicGenerator().update_vodeclic_courses(courses_id_en, organization, 'en')
