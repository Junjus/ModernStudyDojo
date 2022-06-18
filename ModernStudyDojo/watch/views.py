from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *
from .forms import OrderForm
from .filters import OrderFilter


def watch(request, *args, **kwargs):
    return render(request, "watch.html", {})

def index(request, *args, **kwargs):
    return render(request, "index.html", {})

def login(request):
    form = UserCreationForm()
    context = {'form' : form}
    return render(request, "login.html", context)