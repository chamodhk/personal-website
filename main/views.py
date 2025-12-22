from django.shortcuts import render, get_object_or_404
from .models import SiteSettings, Skill, Certificate, Article

# Create your views here.


def home(request):
    settings = SiteSettings.objects.first()
    articles = Article.objects.order_by('-date')[:3]
    return render(request, "home.html", {
        "settings": settings,
        "articles":articles
    })


