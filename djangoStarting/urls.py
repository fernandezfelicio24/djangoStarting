
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('about/', include('about.urls')),
    path('blog/',include('blog.urls')),

    path('admin/', admin.site.urls),
    path('', views.index),

]
