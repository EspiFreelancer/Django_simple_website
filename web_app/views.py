from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = "web_app/index.html"

class Servicios(TemplateView):
    template_name = "web_app/servicios.html"

class Tienda(TemplateView):
    template_name = "web_app/tienda.html"

class Blog(TemplateView):
    template_name = "web_app/blog.html"

class Contacto(TemplateView):
    template_name = "web_app/contacto.html"



# def index(request):
# 	context = {}
# 	# return render(request, 'index.html', context,)
# 	return HttpResponse("Index Page")
