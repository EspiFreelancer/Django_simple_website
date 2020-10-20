from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView

# Create your views here.

class Blog(TemplateView):
    template_name = "blog_app/blog.html"