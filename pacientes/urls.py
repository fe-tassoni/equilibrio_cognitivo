from django.urls import path
from . import views

urlpatterns = [
    path("novo/", views.paciente_create, name="paciente_create"),
    path("lista/", views.paciente_list, name="paciente_list"),
    path("<int:pk>/", views.paciente_detail, name="paciente_detail"),
    path("<int:pk>/editar/", views.paciente_edit, name="paciente_edit"),
    path("<int:pk>/excluir/", views.paciente_delete, name="paciente_delete"),
]


