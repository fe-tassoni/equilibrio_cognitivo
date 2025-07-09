from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pacientes.models import Paciente
from fdt.models import FdtResultados
from django.utils import timezone

def home(request):
    if request.user.is_authenticated:
        pacientes = Paciente.objects.filter(psicologo=request.user).order_by('nome_completo')
        resultados = FdtResultados.objects.filter(id_psicologo=request.user.id).order_by('-data_resultado')
        pacientes_dict = {p.id: p for p in pacientes}
        resultados_list = []
        for r in resultados:
            nome_paciente = pacientes_dict[r.id_paciente].nome_completo if r.id_paciente in pacientes_dict else 'Paciente não encontrado'
            resultados_list.append({
                'pk': r.pk,
                'nome_paciente': nome_paciente,
                'data_resultado': r.data_resultado,
            })
        context = {
            'pacientes': pacientes,
            'resultados': resultados_list,
        }
    else:
        context = {}
    return render(request, 'home/home.html', context)

@login_required
def dashboard(request):
    user = request.user
    pacientes = Paciente.objects.filter(psicologo=user).order_by('nome_completo')
    resultados = FdtResultados.objects.filter(id_psicologo=user.id).order_by('-data_resultado')
    pacientes_dict = {p.id: p for p in pacientes}
    # Cria uma lista de resultados já com o nome do paciente resolvido
    resultados_list = []
    for r in resultados:
        nome_paciente = pacientes_dict[r.id_paciente].nome_completo if r.id_paciente in pacientes_dict else 'Paciente não encontrado'
        resultados_list.append({
            'pk': r.pk,
            'nome_paciente': nome_paciente,
            'data_resultado': r.data_resultado,
        })
    context = {
        'pacientes': pacientes,
        'resultados': resultados_list,
    }
    return render(request, 'home/home.html', context)
