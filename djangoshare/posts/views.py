# from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render

from .models import Category, Post

class CategoryListView(ListView):
    model = Category
    template_name = 'posts/index.html'
    context_object_name = 'category_list'
    ordering = ['category_name']

class CategoryDetailView(ListView):
    model = Post
    template_name = 'posts/category_detail.html'
    context_object_name = 'all_posts'
    ordering = ['title']

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'posts_in_category'

class PostCreateView(CreateView):
    model = Post
    fields = ['category', 'image', 'title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def posts(request):
    pass

def about(request):
    return HttpResponse("About")
