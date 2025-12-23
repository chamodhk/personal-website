from .models import SiteSettings

def navbar_context(request):
    settings = SiteSettings.objects.first()
    return {
        "last_update_date": 
            settings.last_update,
        "first_name": settings.first_name,
        "last_name": settings.last_name,
        "middle_name":settings.middle_name
    }