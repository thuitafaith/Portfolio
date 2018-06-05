from django.db import models

# Create your models here.
"""
Initializing Project Model

"""
class Project(models.Model):
    project_title = models.CharField(max_length=255, null=True, blank=True)
    project_link = models.CharField(max_length=255, null=True, blank=True)
    project_picture = models.ImageField(upload_to='pics/', blank=True, null=True)
    project_description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.project_title)
