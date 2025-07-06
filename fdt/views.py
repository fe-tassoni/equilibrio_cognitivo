from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ResultadoFDTForm

@login_required
def resultado_fdt_create(request):
    # Passamos o usuário logado para o formulário, para que ele possa filtrar os pacientes.
    form = ResultadoFDTForm(request.POST or None, user=request.user)

    if request.method == 'POST':
        if form.is_valid():
            resultado = form.save(commit=False)
            # O psicólogo já é o usuário logado, definido no formulário.
            resultado.psicologo = request.user
            
            # AQUI: Adicionar a lógica para calcular os campos de percentil e classificação
            # Exemplo: resultado.tempo_leitura_pc = calcular_percentil(...)
            
            resultado.save()
            messages.success(request, 'Resultado FDT cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar. Por favor, verifique os campos destacados.')

    context = {
        'form': form,
    }
    return render(request, 'fdt/create.html', context)
