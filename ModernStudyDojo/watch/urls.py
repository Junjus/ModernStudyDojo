from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('watch/', views.watch, name='watch'),
    path('login/', views.login, name='login'),
    path('upload/', views.uploadVideo, name='uploadVideo'),
]