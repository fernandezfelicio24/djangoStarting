
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('soccer/', views.soccer),
    path('story/', views.story),
    path('news/', views.news),
    path('recent/', views.recent),
]

