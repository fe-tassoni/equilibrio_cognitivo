from django.contrib import admin
from .models import FdtResultados


@admin.register(FdtResultados)
class FdtResultadosAdmin(admin.ModelAdmin):
	pass