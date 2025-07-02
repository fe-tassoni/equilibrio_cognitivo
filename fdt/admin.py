from django.contrib import admin
from .models import CorrecaoFDT


@admin.register(CorrecaoFDT)
class CorrecaoFDTAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'fase', 'faixa_etaria_min', 'faixa_etaria_max']
    ordering = ['tipo', 'fase', 'faixa_etaria_min']
