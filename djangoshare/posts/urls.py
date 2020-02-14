from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.category, name="category"),
    path('<int:category_id/posts/', views.posts, name='posts'),
    path('about/', views.about, name='about'),
]