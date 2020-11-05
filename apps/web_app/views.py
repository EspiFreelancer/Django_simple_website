from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = "web_app/index.html"

class Tienda(TemplateView):
    template_name = "web_app/tienda.html"
