from django.urls import path
from . import views

app_name = 'about'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.handle_id),
    path('profile/', views.companyprf, name="profile"),
    path('misaun/', views.companmsn, name="misaun"),
    path('visaun/', views.companyvsn, name="visaun"),
    path('special/<str:input>/', views.aboutsps, name="special"),

    path('about-form/', views.aboutform, name="aboutform"),
]



