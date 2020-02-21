from django.urls import path
from .views import (
    CategoryListView, 
    CategoryDetailView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
    Search
)
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('category/post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('new/', login_required(PostCreateView.as_view()), name='post-create'),
    path('category/post/<int:pk>/update/', login_required(PostUpdateView.as_view()), name='post-update'),
    path('category/post/<int:pk>/delete/', login_required(PostDeleteView.as_view()), name='post-delete'),
    
    path('search/', Search.as_view(), name='search'),
]