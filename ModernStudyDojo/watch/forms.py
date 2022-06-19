from dataclasses import fields
from django import forms

from . import models

class VideoForm(forms.ModelForm):
    class Meta:
        model = models.Video
        fields = [
            'title',
            'video',
        ]