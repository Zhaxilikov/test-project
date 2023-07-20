from django.urls import path

from . import views

urlpatterns = [
    path('', views.Adm_index, name='Adm_home'),
    path('post', views.post_index, name='post_index'),
    path('post_created', views.post_created, name='post_created'),
    path('add_post', views.post_created, name='add_post'),
    path('post_edit', views.post_edit, name='post_edit'),
]