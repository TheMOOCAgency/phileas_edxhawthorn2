from student.models import UserProfile
"""
SOCIAL_AUTH_PIPELINE Additional Step for Amundi
"""

def create_tma_user_profile(backend, user, response, *args, **kwargs):
    if backend.name =='amundi':
        profile=UserProfile(user=user)
        is_manager=response.get('is_manager')
        if is_manager=="true":
            profile.is_manager = True
        else :
            profile.is_manager = False
        custom_field = profile.get('custom_field',{})
        custom_field.update(response)
        profile.custom_field=custom_field
        profile.save()
