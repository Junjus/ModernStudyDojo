from django.shortcuts import render


# Create your views here.
def watch(request, *args, **kwargs):
    return render(request, "watch.html", {})

def index(request, *args, **kwargs):
    return render(request, "index.html", {})

def login(request, *args, **kwargs):
    return render(request, "login.html", {})