from django.db import models

from . import utilities

# Create your models here.
"""
class Course(models.Model):
    listOfVideos =
    name = models.CharField(max_length=120)
    type = 
    subject =
    topic = 
    publishDate = models.DateTimeField()
"""

class Video(models.Model):
    video = models.FileField(upload_to='video/', null=True, verbose_name="")
    title = models.CharField(max_length=120)
    #script = models.
    #exercieses = 
    #comments = 
    def __str__(self):
        return self.title
    
"""
class Comments():
    publishDate = models.DateTimeField()
    updateDate = models.DateTimeField()
    text = models.TextField()
    refernce = 
"""