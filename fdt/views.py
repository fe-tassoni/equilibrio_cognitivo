from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ResultadoFDTForm
from .models import FdtReferencia, FdtResultados
from django.http import HttpResponse
from django.utils import timezone

def calcular_idade(data_nascimento, data_referencia):
    return data_referencia.year - data_nascimento.year - (
        (data_referencia.month, data_referencia.day) < (data_nascimento.month, data_nascimento.day)
    )

def buscar_referencia(tipo, fase, idade, escolaridade=None):
    qs = FdtReferencia.objects.filter(
        tipo=tipo,
        fase=fase,
        faixa_etaria_min__lte=idade,
        faixa_etaria_max__gte=idade
    )
    return qs.first()

def classificar_percentil(valor, referencia):
    if valor <= referencia.pc_95:
        return 95, "Muito acima"
    elif valor <= referencia.pc_75:
        return 75, "Acima"
    elif valor <= referencia.pc_50:
        return 50, "Médio"
    elif valor <= referencia.pc_25:
        return 25, "Abaixo"
    elif valor <= referencia.pc_5:
        return 5, "Muito abaixo"
    else:
        return 0, "Extremo"

@login_required
def resultado_fdt_create(request):
    form = ResultadoFDTForm(request.POST or None, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            resultado = form.save(commit=False)
            # Ajusta para o timezone local configurado no Django
            resultado.data_resultado = timezone.localtime(timezone.now())
            paciente = form.cleaned_data['paciente']
            escolaridade = paciente.escolaridade
            idade = calcular_idade(paciente.data_nascimento, resultado.data_resultado.date())

            fases_tempos = [
                ('Leitura', 'Leitura'),
                ('Contagem', 'Contagem'),
                ('Escolha', 'Escolha'),
                ('Alternancia', 'Alternância'),
                ('Inibicao', 'Inibição'),
                ('Flexibilidade', 'Flexibilidade'),
            ]
            tempo_pc_dict = {}
            tempo_class_dict = {}
            for attr_fase, db_fase in fases_tempos:
                valor = getattr(resultado, f'tempo_{attr_fase.lower()}')
                if valor is None or (isinstance(valor, str) and not valor.strip()):
                    pc, classe = 0, 'Sem referência'
                else:
                    try:
                        valor_num = float(valor)
                    except (ValueError, TypeError):
                        pc, classe = 0, 'Sem referência'
                    else:
                        ref = buscar_referencia('Tempos', db_fase, idade, escolaridade)
                        if ref:
                            pc, classe = classificar_percentil(valor_num, ref)
                        else:
                            pc, classe = 0, 'Sem referência'
                setattr(resultado, f'tempo_{attr_fase.lower()}_pc', pc)
                setattr(resultado, f'tempo_{attr_fase.lower()}_class', classe)
                tempo_pc_dict[attr_fase] = pc
                tempo_class_dict[attr_fase] = classe

            fases_erros = [
                ('Leitura', 'Leitura'),
                ('Contagem', 'Contagem'),
                ('Escolha', 'Escolha'),
                ('Alternancia', 'Alternância'),
            ]
            for attr_fase, db_fase in fases_erros:
                valor = getattr(resultado, f'erro_{attr_fase.lower()}')
                if attr_fase in ['Leitura', 'Contagem']:
                    if valor == 0:
                        pc = tempo_pc_dict.get(attr_fase, 0)
                        classe = tempo_class_dict.get(attr_fase, 'Sem referência')
                    else:
                        pc, classe = 5, 'Muito abaixo'
                else:
                    ref = buscar_referencia('Erros', db_fase, idade, escolaridade)
                    if ref:
                        pc, classe = classificar_percentil(valor, ref)
                    else:
                        pc, classe = 0, 'Sem referência'
                setattr(resultado, f'erro_{attr_fase.lower()}_pc', pc)
                setattr(resultado, f'erro_{attr_fase.lower()}_class', classe)

            # campos = [f"{field.name}: {getattr(resultado, field.name)}" for field in resultado._meta.fields]
            # return HttpResponse("<pre>" + "\n".join(campos) + "</pre>")

            resultado.id_paciente = paciente.id
            resultado.id_psicologo = request.user.id
            resultado.save()
            messages.success(request, 'Resultado FDT cadastrado com sucesso!')
            return redirect('fdt_detail', pk=resultado.pk)
        
        else:
            error_msgs = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_msgs.append(f"{field}: {error}")
            messages.error(request, 'Erro ao cadastrar: ' + ' | '.join(error_msgs))


    context = {'form': form}
    return render(request, 'fdt/create.html', context)

@login_required
def resultado_fdt_detail(request, pk):
    resultado = get_object_or_404(FdtResultados, pk=pk)
    context = {'resultado': resultado}
    return render(request, 'fdt/detail.html', context)
