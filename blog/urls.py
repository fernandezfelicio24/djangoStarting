
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('soccer/', views.soccer),
    #path('buisnes/', views.buisnes),
    path('news/', views.news),
    path('jurnal/', views.jurnal),
    path('gossip/', views.gossip),
]

