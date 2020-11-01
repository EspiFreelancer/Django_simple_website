from django import template
from apps.pages_app.models import Generic_page

register = template.Library()

@register.simple_tag
def get_page_list():
	pages = Generic_page.objects.all()
	return pages