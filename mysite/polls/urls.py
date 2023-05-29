
from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_all_music', views.get_all_music, name='get_all_music'),
    path('like-track', views.like_track, name='like_track'),
    re_path(r'^music/', views.music, name='music'),
]