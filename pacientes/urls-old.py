from django.urls import path
from . import views

urlpatterns = [
    path("novo/", views.paciente_create, name="paciente_create"),
    path("lista/", views.paciente_list, name="paciente_list"),
]


