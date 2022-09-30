
from django.contrib import admin
from django.urls import path, include

#import using for Template View
from django.views.generic.base import TemplateView, RedirectView

from . import views
from .views import IndexClassView, ContextView, ParameterView, HomeView , HomeRedirectView

urlpatterns = [

    path('about/', include('about.urls', namespace='about')),
    path('blog/',include('blog.urls', namespace='blog')),

    path('admin/', admin.site.urls),
    path('', views.index, name="index"),

    path('test-form', views.testform, name="tesform"),

    #url for the class based view
    path('test-base', views.testbase, name="testbase"),
    path('test-class/based-view', IndexClassView.as_view(template_name='testbase1.html'), name="classbasedview"),
    path('test-clas s2/based-view2', IndexClassView.as_view(template_name='testbase2.html'), name="classbasedview2"),

    #url for the template view
    path('template-view', TemplateView.as_view(template_name='templateview.html'), name="templateview"),

    #url for the context view
    path('context-view', ContextView.as_view(), name="contextview"),

    #url for parameter view
    path('parameter-view/<str:parameter1>/<str:parameter2>/', ParameterView.as_view(), name="category"),

    #this url bellow for learning redirect view

    path('home', RedirectView.as_view(url='/'), name="homeredirect"),
    path('rumah', RedirectView.as_view(pattern_name='homeredirect'), name="rumahredirect"),
    path('home/', HomeView.as_view(), name="homeview"),

    #this url of redirect view doesnt work
    path('home/<str:nameinput>', HomeRedirectView.as_view(), name="homeredirectview"),
    #path('fuck', TemplateView.as_view(template_name='testForm.html')),
]