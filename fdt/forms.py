from django import forms
from .models import FdtResultados
from pacientes.models import Paciente

class ResultadoFDTForm(forms.ModelForm):
    # 1. CAMPO 'paciente' CUSTOMIZADO
    # O modelo tem 'id_paciente' como um IntegerField. Para mostrar um dropdown
    # com nomes de pacientes, criamos um campo separado e não mapeado no formulário.
    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),
        label="Paciente Avaliado",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = FdtResultados
        
        # 2. LISTA DE CAMPOS CORRETA
        # Estes são os campos que o Django tentará salvar no modelo.
        # Note que 'paciente' (o campo customizado) não está aqui.
        fields = [
            # 'data_resultado',
            'tempo_leitura', 'erro_leitura',
            'tempo_contagem', 'erro_contagem',
            'tempo_escolha', 'erro_escolha',
            'tempo_alternancia', 'erro_alternancia',
            'tempo_inibicao',
            'tempo_flexibilidade',
        ]

        # 3. LABELS CORRETOS
        # Apenas para os campos que precisam de um label visível.
        labels = {
            # 'data_resultado': 'Data de Aplicação do Teste',
            # Labels para os campos da tabela são vazios, pois o cabeçalho da tabela já os descreve.
            'tempo_leitura': '', 'erro_leitura': '',
            'tempo_contagem': '', 'erro_contagem': '',
            'tempo_escolha': '', 'erro_escolha': '',
            'tempo_alternancia': '', 'erro_alternancia': '',
            'tempo_inibicao': '',
            'tempo_flexibilidade': '',
        }

        # 4. WIDGETS CORRETOS
        # Widgets para estilizar os campos do formulário.
        widgets = {
            # 'data_resultado': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            
            # Inputs para as tabelas (menores e centralizados)
            'tempo_leitura': forms.NumberInput(attrs={'class': 'form-control form-control-sm text-center'}),
            'erro_leitura': forms.NumberInput(attrs={'class': 'form-control form-control-sm text-center'}),
            'tempo_contagem': forms.NumberInput(attrs={'class': 'form-control form-control-sm text-center'}),
            'erro_contagem': forms.NumberInput(attrs={'class': 'form-control form-control-sm text-center'}),
            'tempo_escolha': forms.NumberInput(attrs={'class': 'form-control form-control-sm text-center'}),
            'erro_escolha': forms.NumberInput(attrs={'class': 'form-control form-control-sm text-center'}),
            'tempo_alternancia': forms.NumberInput(attrs={'class': 'form-control form-control-sm text-center'}),
            'erro_alternancia': forms.NumberInput(attrs={'class': 'form-control form-control-sm text-center'}),
            'tempo_inibicao': forms.NumberInput(attrs={'class': 'form-control form-control-sm text-center'}),
            'tempo_flexibilidade': forms.NumberInput(attrs={'class': 'form-control form-control-sm text-center'}),
            # Oculta todos os campos *_pc e *_class
            'tempo_leitura_pc': forms.HiddenInput(),
            'tempo_leitura_class': forms.HiddenInput(),
            'tempo_contagem_pc': forms.HiddenInput(),
            'tempo_contagem_class': forms.HiddenInput(),
            'tempo_escolha_pc': forms.HiddenInput(),
            'tempo_escolha_class': forms.HiddenInput(),
            'tempo_alternancia_pc': forms.HiddenInput(),
            'tempo_alternancia_class': forms.HiddenInput(),
            'tempo_inibicao_pc': forms.HiddenInput(),
            'tempo_inibicao_class': forms.HiddenInput(),
            'tempo_flexibilidade_pc': forms.HiddenInput(),
            'tempo_flexibilidade_class': forms.HiddenInput(),
            'erro_leitura_pc': forms.HiddenInput(),
            'erro_leitura_class': forms.HiddenInput(),
            'erro_contagem_pc': forms.HiddenInput(),
            'erro_contagem_class': forms.HiddenInput(),
            'erro_escolha_pc': forms.HiddenInput(),
            'erro_escolha_class': forms.HiddenInput(),
            'erro_alternancia_pc': forms.HiddenInput(),
            'erro_alternancia_class': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        # Recebe o usuário da view para filtrar a lista de pacientes
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Reordena os campos para que 'paciente' apareça primeiro
        field_order = ['paciente'] + self.Meta.fields
        self.order_fields(field_order)

        if user:
            # Filtra o queryset do nosso campo customizado 'paciente'
            self.fields['paciente'].queryset = Paciente.objects.filter(psicologo=user).order_by('nome_completo')

    def save(self, commit=True):
        # 5. MÉTODO SAVE CUSTOMIZADO
        # Precisamos interceptar o processo de salvar para popular os campos de ID.
        
        # Pega a instância do modelo, mas não salva no banco ainda.
        instance = super().save(commit=False)
        
        # Pega o objeto Paciente selecionado no nosso campo customizado.
        paciente_selecionado = self.cleaned_data.get('paciente')
        if paciente_selecionado:
            # Atribui o ID do paciente e do psicólogo ao modelo.
            instance.id_paciente = paciente_selecionado.id
            instance.id_psicologo = paciente_selecionado.psicologo.id

        # AQUI: Futuramente, você adicionará a lógica para calcular e preencher
        # todos os campos de percentil (_pc) e classificação (_class).
        # Ex: instance.tempo_leitura_pc = calcular_pc(instance.tempo_leitura)
        
        if commit:
            instance.save()
            
        return instance
