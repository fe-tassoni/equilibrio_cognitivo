from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):

    # Este campo existe apenas no formulário, não no modelo Paciente.
    idade = forms.CharField(
        label="Idade (calculada automaticamente)",
        required=False,  # Não é obrigatório preencher
        widget=forms.TextInput(
            attrs={
                "readonly": "readonly",  # Impede que o usuário edite o campo
                "id": "id_idade",  # Define um ID fixo para o JavaScript encontrar
                "placeholder": "A idade será calculada após inserir a data de nascimento",
                "style": "background-color: #e9ecef;",  # Estilo visual para parecer desabilitado
            }
        ),
    )

    class Meta:
        model = Paciente
        fields = [
            "nome_completo",
            "data_nascimento",
            'idade',
            "escolaridade",
            "sexo",
            "estado_civil",
            "profissao",
            "telefone",
            "observacoes",
        ]
        widgets = {
            "nome_completo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nome completo"}
            ),
            "data_nascimento": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "escolaridade": forms.Select(attrs={"class": "form-select"}),
            "sexo": forms.Select(attrs={"class": "form-select"}),
            "estado_civil": forms.Select(attrs={"class": "form-select"}),
            "profissao": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Profissão"}
            ),
            "telefone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Telefone"}
            ),
            "observacoes": forms.Textarea(
                attrs={"class": "form-control", "rows": 3, "placeholder": "Observações"}
            ),
        }
