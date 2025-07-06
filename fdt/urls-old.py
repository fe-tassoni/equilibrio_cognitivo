from django.urls import path
from . import views

urlpatterns = [
    path("novo/", views.resultado_fdt_create, name="resultado_fdt_create"),
]


