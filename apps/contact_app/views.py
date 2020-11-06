
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
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

        body = render_to_string(
            'contact_app/email_content.html', {
            'name': name,
            'email': email,
            'message': message,
            },
        )

        email_message = EmailMessage(
            subject='Mensaje de usuario',
            body= body,
            from_email=email,
            to=['email.de.prueba@gmail.com'],
        )
        email_message.content_subtype = 'html'
        email_message.send()

        return redirect('contact:contact')