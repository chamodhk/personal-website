from django.db import models

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
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    completed_date = models.DateField(auto_now_add=True)
    article_link = models.URLField()
    github_link = models.URLField()
    skills = models.ManyToManyField(Skill, related_name="projects")

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    body = models.TextField()
    medium_link = models.URLField(blank=True)
    github_link = models.URLField()
    youtube_link = models.URLField(blank=True)

    def __str__(self):
        return self.name
    


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

