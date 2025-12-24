from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
from taggit.managers import TaggableManager


# Create your models here.

class Skill(models.Model):
    SKILL_TYPES = [
        ("language", "Programming Language"),
        ("framework", "Framework"),
        ("tool", "Tool"),
        ("soft", "Soft Skill"),
        ("other", "Other"),
    ]
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=SKILL_TYPES)

    def __str__(self) -> str:
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    institute = models.CharField(max_length=50)
    issued_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(blank=True)
    skills = models.ManyToManyField(Skill, related_name="certificates")

    def __str__(self) -> str:
        return f"{self.name} from {self.institute}"
    

class Project(models.Model):
    PROJECT_CATEGORIES = [
        ("academic", "Academic"),
        ("personal", "Personal / Hobby"),
        ("research", "Research"),
        ("open_source", "Open Source"),
        ("experimental", "Experimental"),
        ("freelance", "Freelance / Client"),
        ("learning", "Learning / Practice"),
    ]


    name = models.CharField(max_length=150)
    description = models.TextField()
    completed_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=30, choices=PROJECT_CATEGORIES, default="personal")
    article_link = models.URLField()
    github_link = models.URLField()
    skills = models.ManyToManyField(Skill, related_name="projects")

    tags = TaggableManager(blank=True)

    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=50)
    date = models.DateTimeField()
    slug=AutoSlugField(populate_from='title', unique_with="date__month")


    body = models.TextField()

    tags = TaggableManager(blank=True)
    medium_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)


    view_count = models.IntegerField(default=0)
    claps = models.IntegerField(default=0)

   

    def __str__(self):
        return self.title

    


class SiteSettings(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100, blank=True)
    email = models.EmailField()

    subtitle = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True)
    last_update = models.DateField(auto_now=True)

    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)


    def __str__(self) -> str:
        return "Site Settings"

