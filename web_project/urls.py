"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView # To use in permanent redirect

# Use to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static




# Global URLconf
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Web_App URLconf
urlpatterns += [
	path('', include('web_app.urls', namespace='web')),
    path('', include('services_app.urls', namespace='services')),
]

# Use static() to add url mapping to serve static files during development (only)
if settings.DEBUG is True:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)