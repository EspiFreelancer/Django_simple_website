from django.contrib import admin
from .models import Services

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    '''
        Admin View for Services
    '''
    readonly_fields = ('created', 'updated')


admin.site.register(Services, ServicesAdmin)

