from openedx.core.djangoapps.theming.helpers import get_current_site
import json

import logging
log = logging.getLogger()


class ZoneManager():
    def __init__(self, user):
        self.user=user
        self.user_custom_field = self.getCustomField()
    
    def getCustomField(self):
        try:
            user_custom_field = json.loads(self.user.profile.custom_field)
        except:
            user_custom_field={}
        return user_custom_field

    def get_user_zone(self):
        zones_infos=""
        with open("/edx/app/edxapp/edx-platform/lms/djangoapps/tma_apps/zones/zones_infos.json") as zone_file :
            zone_infos = zone_file.read()
        user_zone = json.loads(zone_infos).get(str(self.user_custom_field.get('zoneinfo')).lower())
        return user_zone

    def check_zone(self):
        current_site = get_current_site()
        user_zone = self.get_user_zone()
        return user_zone is not None and (user_zone.lower()!=str(current_site).lower().split('.')[0])

