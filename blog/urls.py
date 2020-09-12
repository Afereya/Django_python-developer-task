from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name="blog"),
    path('post/<int:id>/', views.post, name='post'),
    # path('search/', views.search, name="search"),
    # path('create/', views.create, name="create"),
    # path('update/', views.update_, name="update"),
    # path('delete/', views.delete_, name="delete"),
    path('tags/', views.tags_list, name='tags_list_url'),
    path('tag/<str:slug>', views.tag_detail, name='tag_detail_url'),
]

