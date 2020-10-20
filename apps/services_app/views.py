from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from .models import Services

# Create your views here.

class Servicio(ListView):
    """
    Services list CBV 
    """
    model = Services
    template_name = "services_app/servicios.html"
