from django.views.generic import TemplateView
from django.shortcuts import redirect

from .forms import ContactForm

# Create your views here.

class ContactView(TemplateView):
    template_name = "contact_app/contacto.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        
        return context

    def post(self, request, *args, **kwargs):
    	name = request.POST.get('name')
    	email = request.POST.get('email')
    	message = request.POST.get('message')

    	print('===================')
    	print(name)
    	print(email)
    	print(message)
    	print('===================')

    	return redirect('web:index')