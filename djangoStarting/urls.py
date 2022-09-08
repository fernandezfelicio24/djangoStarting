
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('about/', include('about.urls', namespace='about')),
    path('blog/',include('blog.urls', namespace='blog')),

    path('admin/', admin.site.urls),
    path('', views.index, name="index"),

]
