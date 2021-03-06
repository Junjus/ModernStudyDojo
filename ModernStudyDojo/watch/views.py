from multiprocessing import context
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Import Models
from . import forms
from . import models 
from . import utilities


# Create your views here.
def watch(request):
    video = models.Video.objects.all()
    return render(request, "watch.html", {"video": video})

"""
@ensure_csrf_cookie
def uploadVideo(request):
    if request.method == 'POST':
        print("Post")
            
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print(file.name)
            utilities.handle_uploaded_file(request.FILES['file'])
            return uploadedSuccessfully
        
    else:
        print("Not Post")
        form = VideoForm()

    #return render(request, "uploadVideo.html", {'form': form})
    return render(request, "uploadVideo.html", {})
"""
def uploadVideo(request):
    form = forms.VideoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "uploadVideo.html", context)

def uploadedSuccessfully(request):
    return render(request, "uploadedSuccessfully.html", {})



def index(request, *args, **kwargs):
    return render(request, "index.html", {})


def login(request):
    form = UserCreationForm()
    context = {'form' : form}
    return render(request, "login.html", context)

def register(request, *args, **kwargs):
    return render(request, "register.html", {})
