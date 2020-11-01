from django.contrib import admin
from .models import Generic_page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	pass

admin.site.register(Generic_page, PageAdmin)