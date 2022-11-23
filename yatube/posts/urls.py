from django.urls import path, include

from . import views
app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group_posts, name='group_posts'),
    path('group/<slug:slug>/', views.group_posts),    
]