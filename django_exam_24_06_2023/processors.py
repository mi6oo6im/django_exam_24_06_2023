from .webapp.models import UserProfile


def get_profile(request):
    profile = UserProfile.objects.first()
    return {'profile': profile}
