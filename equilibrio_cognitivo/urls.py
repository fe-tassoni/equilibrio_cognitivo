"""
URL configuration for equilibrio_cognitivo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(\'\', views.home, name=\'home\')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(\'\', Home.as_view(), name=\'home\')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path(\'blog/\', include(\'blog.urls\'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # página inicial
    path('usuarios/', include('usuarios.urls')),  # URLs customizadas de usuários
    path('accounts/', include('allauth.urls')),  # URLs do allauth (login social, etc.)
    path('fdt/', include('fdt.urls')),  # FDT app
    path('pacientes/', include('pacientes.urls')),  # Pacientes app
    
    # Páginas estáticas
    path('termos/', TemplateView.as_view(template_name='pages/terms.html'), name='terms'),
    path('privacidade/', TemplateView.as_view(template_name='pages/privacy.html'), name='privacy'),
    path('sobre/', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    path('contato/', TemplateView.as_view(template_name='pages/contact.html'), name='contact'),


]

# Servir arquivos de media em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0] if settings.STATICFILES_DIRS else None)

