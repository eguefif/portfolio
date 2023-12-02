from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField("date finished")
    url = models.URLField(max_length=240)
    description = models.TextField(max_length = 2500)

    def __str__(self):
        return self.title
