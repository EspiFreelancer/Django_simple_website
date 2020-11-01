from django.shortcuts import render, get_object_or_404
from .models import Generic_page

# Create your views here.

def generic_page(request, page_id, page_slug):
	page =  get_object_or_404(Generic_page, id=page_id)
	return render(request, 'pages_app/generic_page.html', {'page':page})