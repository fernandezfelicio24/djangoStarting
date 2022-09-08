
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:categoryInput>/', views.categoryPost),
    path('post/<slug:slugInput>/', views.singlePost),
    path('detail-post/<slug:slugInput>/', views.detailPost),
    path('category/<str:categoryInput>/', views.categoryPostingan, name="category"),
    #path('<int:id>/', views.handle_id),
    path('soccer/', views.soccer),
    #path('buisnes/', views.buisnes),
    path('news/', views.news),
    path('jurnal/', views.jurnal),
    path('gossip/', views.gossip),

]

