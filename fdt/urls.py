from django.urls import path
from . import views

urlpatterns = [
    path("novo/", views.resultado_fdt_create, name="fdt_create"),
    path("<int:pk>/", views.resultado_fdt_detail, name="fdt_detail"),
]


