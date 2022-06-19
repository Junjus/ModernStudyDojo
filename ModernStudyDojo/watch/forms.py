from django import forms


class VideoForm(forms.Form):
    title = forms.CharField(max_length=120)
    file = forms.FileField()
    #script = forms.FileField()
    #exercieses = 
    #comments = 