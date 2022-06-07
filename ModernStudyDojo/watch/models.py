from django.db import models

# Create your models here.
class Video(models.Model):
    videoID = models.CharField(max_length=120)
    videoFile = models.FileField
    