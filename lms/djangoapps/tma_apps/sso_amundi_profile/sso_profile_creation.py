from student.models import UserProfile
import json
"""
SOCIAL_AUTH_PIPELINE Additional Step for Amundi
"""

def create_tma_user_profile(backend, user, response, *args, **kwargs):
    if backend.name =='amundi':
        is_manager=response.get('is_manager')

        if UserProfile.objects.filter(user=user).exists():
          profile=UserProfile.objects.get(user=user)
        else :
          profile=UserProfile(user=user)

        try :
            custom_field = json.loads(profile.custom_field)
        except:
            custom_field={}
        try:
            if not profile.rpid:
                profile.rpid=response.get('rpid','')
            if not profile.iug:
                profile.iug=response.get('iug','')
        except:
            pass

        if is_manager!="false" or is_manager:
            profile.is_manager = True
        else :
            profile.is_manager = False

        custom_field.update(response)
        profile.custom_field=json.dumps(custom_field)
        profile.save()
