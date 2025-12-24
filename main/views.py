from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import SiteSettings, Skill, Certificate, Article
from django.db.models import Q


# Create your views here.


def home(request):
    settings = SiteSettings.objects.first()
    articles = Article.objects.order_by('-date')[:3]
    return render(request, "home.html", {
        "settings": settings,
        "articles":articles
    })


def blog_home(request):
    articles = Article.objects.all().order_by('-date')
    query = request.GET.get("q", "")
    tag_query = request.GET.get("tag","")

    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(subtitle__icontains=query) |
            Q(body__icontains=query)
        )

    if tag_query:
        articles = articles.filter(
            tags__name__in=[tag_query]
        )

    paginator = Paginator(articles,5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,"bloghome.html", {"page":page, "query":query})

def get_article(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    article.view_count += 1
    article.save()
    recent_articles=Article.objects.order_by('-date')[:4]
    context = {'article': article, 'recents':recent_articles}
    return render(request,"post.html",context)