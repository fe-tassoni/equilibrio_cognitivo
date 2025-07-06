from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FdtResultados

@login_required
def resultado_fdt_detail(request, pk):
    resultado = get_object_or_404(FdtResultados, pk=pk)
    context = {'resultado': resultado}
    return render(request, 'fdt/detail.html', context)
