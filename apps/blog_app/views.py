from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView, DetailView
from .models import Post, Category

# Create your views here.

class BlogList(ListView):
    """
    CBV to list all posts
    """
    model = Post
    template_name = "blog_app/blog.html"

def category(request, id):
	"""
	List posts by PK of category
	"""
	category = Category.objects.get(id=id)
	posts = Post.objects.filter(category=category)
	return render(request, "blog_app/post_list.html", {'category':category,"posts":posts})