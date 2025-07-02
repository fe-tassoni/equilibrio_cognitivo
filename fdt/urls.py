from django.urls import path
from . import views

urlpatterns = [
    path('', views.fdt_list, name='fdt_list'),
    path('novo/', views.fdt_create, name='fdt_create'),
    path('<int:pk>/', views.fdt_detail, name='fdt_detail'),
    path('<int:pk>/editar/', views.fdt_edit, name='fdt_edit'),
    path('<int:pk>/deletar/', views.fdt_delete, name='fdt_delete'),
    path('<int:pk>/relatorio/', views.fdt_report, name='fdt_report'),
]

