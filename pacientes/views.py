from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Paciente

@login_required
def paciente_list(request):
    """Lista todos os pacientes do usuário"""
    pacientes = Paciente.objects.filter(psicologo=request.user).order_by('nome_completo')
    context = {
        'pacientes': pacientes,
    }
    return render(request, 'pacientes/list.html', context)

@login_required
def paciente_create(request):
    """Cria um novo paciente"""
    if request.method == 'POST':
        # Implementar lógica de criação com formulário
        messages.success(request, 'Paciente cadastrado com sucesso!')
        return redirect('paciente_list')
    
    return render(request, 'pacientes/create.html')

@login_required
def paciente_detail(request, pk):
    """Exibe detalhes de um paciente específico"""
    paciente = get_object_or_404(Paciente, pk=pk, psicologo=request.user)
    context = {
        'paciente': paciente,
    }
    return render(request, 'pacientes/detail.html', context)

@login_required
def paciente_edit(request, pk):
    """Edita um paciente existente"""
    paciente = get_object_or_404(Paciente, pk=pk, psicologo=request.user)
    
    if request.method == 'POST':
        # Implementar lógica de edição
        messages.success(request, 'Paciente atualizado com sucesso!')
        return redirect('paciente_detail', pk=pk)
    
    context = {
        'paciente': paciente,
    }
    return render(request, 'pacientes/edit.html', context)

@login_required
def paciente_delete(request, pk):
    """Deleta um paciente"""
    paciente = get_object_or_404(Paciente, pk=pk, psicologo=request.user)
    
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente removido com sucesso!')
        return redirect('paciente_list')
    
    context = {
        'paciente': paciente,
    }
    return render(request, 'pacientes/delete.html', context)

