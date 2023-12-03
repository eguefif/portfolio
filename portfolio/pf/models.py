from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField("date finished")
    github = models.URLField(max_length=240)
    small_description = models.CharField(max_length=200,
            default="")
    description = models.TextField(max_length = 2500)
    image = models.FileField(upload_to="project_images/", blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    project = models.ManyToManyField(Project)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)

class Technology(models.Model):
    project = models.ManyToManyField(Project)
    name = models.CharField(max_length=60)
