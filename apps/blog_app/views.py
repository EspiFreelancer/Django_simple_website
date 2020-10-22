from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from .models import Post

# Create your views here.

class BlogList(ListView):
    """
    Services list CBV 
    """
    model = Post
    template_name = "blog_app/blog.html"