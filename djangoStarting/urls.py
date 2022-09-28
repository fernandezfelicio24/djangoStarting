
from django.contrib import admin
from django.urls import path, include

#import using for Template View
from django.views.generic.base import TemplateView

from . import views
from .views import IndexClassView, ContextView, ParameterView
urlpatterns = [

    path('about/', include('about.urls', namespace='about')),
    path('blog/',include('blog.urls', namespace='blog')),

    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('test-form', views.testform, name="tesform"),

    #url for the class based view
    path('test-base', views.testbase, name="testbase"),
    path('test-class/based-view', IndexClassView.as_view(template_name='testbase1.html'), name="classbasedview"),
    path('test-class2/based-view2', IndexClassView.as_view(template_name='testbase2.html'), name="classbasedview2"),
    
    #url for the template view
    path('template-view', TemplateView.as_view(template_name='templateview.html'), name="templateview"),

    #url for the context view
    path('context-view', ContextView.as_view(), name="contextview"),

    #url for parameter view
    path('parameter-view/<str:parameter1>/<str:parameter2>/', ParameterView.as_view(), name="category"),
]
