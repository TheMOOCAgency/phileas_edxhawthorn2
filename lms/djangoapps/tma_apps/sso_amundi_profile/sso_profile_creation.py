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

        if is_manager=="true":
            profile.is_manager = True
        else :
            profile.is_manager = False

        custom_field.update(response)
        profile.custom_field=json.dumps(custom_field)
        profile.save()
