from django.contrib import admin
from django.db import models
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class ArticleModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)


admin.site.register(Skill)
admin.site.register(Certificate)
admin.site.register(Project)
admin.site.register(Article, ArticleModelAdmin)
admin.site.register(SiteSettings)




