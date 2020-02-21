# from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.db.models import Q


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

class PostUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['category', 'image', 'title', 'description']
    success_message = 'Your post has been deleted!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    success_message = '"%(title)s" was updated succesfully!'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data
        )

class PostDeleteView(SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            print('Your post has been deleted!')
            return True
        return False

    success_message = '"%(title)s" has been deleted!'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data
        )

class Search(ListView):
    model = Post
    template_name = 'posts/search.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list

def posts(request):
    pass

def about(request):
    return HttpResponse("About")
