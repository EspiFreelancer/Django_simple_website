from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView, DetailView
from .models import Post, Category

# Create your views here.

class BlogList(ListView):
    """
    CBV to list all posts.
    """
    model = Post
    template_name = "blog_app/blog.html"

class PostDetailView(DetailView):
    """
    CBV to detail post.
    """
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'url'

def category(request, category_id):
	"""
	List posts by PK of category.
	"""
	category = get_object_or_404(Category, id=category_id)
	return render(request, "blog_app/post_list.html", {'category':category})