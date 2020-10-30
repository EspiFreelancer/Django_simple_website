from django.contrib import admin
from .models import Networks

# Register your models here.

class NetworksAdmin(admin.ModelAdmin):
    pass

admin.site.register(Networks, NetworksAdmin)  