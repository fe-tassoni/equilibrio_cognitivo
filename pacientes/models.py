from django.db import models
from django.contrib.auth.models import User


class Paciente(models.Model):
    psicologo = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    sexo = models.CharField(
        max_length=1,
        choices=[("M", "Masculino"), ("F", "Feminino"), ("O", "Outro")],
    )
    estado_civil = models.CharField(
        max_length=20,
        choices=[
            ("solteiro", "Solteiro(a)"),
            ("casado", "Casado(a)"),
            ("divorciado", "Divorciado(a)"),
            ("viuvo", "Viúvo(a)"),
            ("uniao_estavel", "União Estável"),
        ],
        null=True,
        blank=True,
    )
    escolaridade = models.CharField(
        max_length=50,
        choices=[
            ("fundamental_incompleto", "Ensino Fundamental Incompleto"),
            ("fundamental_completo", "Ensino Fundamental Completo"),
            ("medio_incompleto", "Ensino Médio Incompleto"),
            ("medio_completo", "Ensino Médio Completo"),
            ("superior_incompleto", "Ensino Superior Incompleto"),
            ("superior_completo", "Ensino Superior Completo"),
            ("pos_graduacao", "Pós-Graduação"),
            ("mestrado", "Mestrado"),
            ("doutorado", "Doutorado"),
            ("nao_informado", "Não Informado"),
        ],
        null=True,
        blank=True,
    )
    profissao = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome_completo} ({self.psicologo.username})"
