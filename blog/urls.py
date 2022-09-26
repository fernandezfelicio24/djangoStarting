
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name="index"),
path('create-blog', views.create, name="create_blog"),
    path('store-blog', views.store, name="store_blog"),
    path('delete-blog/<int:delete_id>/', views.destroy, name="destroy"),
    path('edit-blog/<int:edit_id>/', views.edit, name="edit"),
    path('update-form/<int:update_id>', views.update, name="update"),
    path('<str:categoryInput>/', views.categoryPost),
    path('post/<slug:slugInput>/', views.singlePost),
    path('detail-post/<slug:slugInput>/', views.detailPost, name="detail-post"),
    path('category/<str:categoryInput>/', views.categoryPostingan, name="category"),
    #path('<int:id>/', views.handle_id),
    path('soccer/', views.soccer),

    #path('buisnes/', views.buisnes),
    # path('news/', views.news),
    # path('jurnal/', views.jurnal),
    # path('gossip/', views.gossip),

]

