
from django.contrib import admin
from django.urls import path, include



from . import views
from .views import IndexClassView
urlpatterns = [

    path('about/', include('about.urls', namespace='about')),
    path('blog/',include('blog.urls', namespace='blog')),

    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('test-form', views.testform, name="tesform"),

    path('test-base', views.testbase, name="testbase"),
    path('test-class/based-view', IndexClassView.as_view(template_name='testbase1.html'), name="classbasedview"),
    path('test-class2/based-view2', IndexClassView.as_view(template_name='testbase2.html'), name="classbasedview2"),
]
