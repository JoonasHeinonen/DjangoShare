# from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Category

def index(request):
    category_list = Category.objects.order_by('category_name')
    context = {
        'category_list': category_list
    }
    return render(request, 'posts/index.html', context)

def category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'posts/category.html', {'category': category})

def posts(request):
    pass

def login(request):
    return render(request, 'posts/login.html')

def register(request):
    return render(request, 'posts/register.html')

def about(request):
    return HttpResponse("About")
