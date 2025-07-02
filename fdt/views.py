from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import CorrecaoFDT

@login_required
def fdt_list(request):
    """Lista todos os testes FDT do usuário"""
    # Por enquanto, apenas uma página placeholder
    context = {
        'testes': [],  # Será implementado quando tivermos o modelo de teste
    }
    return render(request, 'fdt/list.html', context)

@login_required
def fdt_create(request):
    """Cria um novo teste FDT"""
    if request.method == 'POST':
        # Implementar lógica de criação
        messages.success(request, 'Teste FDT criado com sucesso!')
        return redirect('fdt_list')
    
    return render(request, 'fdt/create.html')

@login_required
def fdt_detail(request, pk):
    """Exibe detalhes de um teste FDT específico"""
    # teste = get_object_or_404(TesteFDT, pk=pk, usuario=request.user)
    context = {
        'teste_id': pk,
    }
    return render(request, 'fdt/detail.html', context)

@login_required
def fdt_edit(request, pk):
    """Edita um teste FDT existente"""
    if request.method == 'POST':
        messages.success(request, 'Teste FDT atualizado com sucesso!')
        return redirect('fdt_detail', pk=pk)
    
    context = {
        'teste_id': pk,
    }
    return render(request, 'fdt/edit.html', context)

@login_required
def fdt_delete(request, pk):
    """Deleta um teste FDT"""
    if request.method == 'POST':
        # Implementar lógica de deleção
        messages.success(request, 'Teste FDT deletado com sucesso!')
        return redirect('fdt_list')
    
    context = {
        'teste_id': pk,
    }
    return render(request, 'fdt/delete.html', context)

@login_required
def fdt_report(request, pk):
    """Gera relatório de um teste FDT"""
    context = {
        'teste_id': pk,
    }
    return render(request, 'fdt/report.html', context)

