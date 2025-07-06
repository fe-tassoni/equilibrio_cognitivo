from django.urls import path
from . import views
from .views_detail import resultado_fdt_detail

urlpatterns = [
    path("novo/", views.resultado_fdt_create, name="fdt_create"),
    path("<int:pk>/", resultado_fdt_detail, name="fdt_detail"),
]


