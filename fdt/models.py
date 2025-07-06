from django.db import models
from django.contrib.auth.models import User
from pacientes.models import Paciente # Importa o modelo Paciente
from django.utils import timezone


class FdtResultados(models.Model):
    id_resultado = models.IntegerField(primary_key=True)
    id_psicologo = models.IntegerField()
    id_paciente = models.IntegerField()
    data_resultado = models.DateTimeField()
    tempo_leitura = models.IntegerField()
    tempo_leitura_pc = models.IntegerField()
    tempo_leitura_class = models.CharField()
    tempo_contagem = models.IntegerField()
    tempo_contagem_pc = models.IntegerField()
    tempo_contagem_class = models.CharField()
    tempo_escolha = models.IntegerField()
    tempo_escolha_pc = models.IntegerField()
    tempo_escolha_class = models.CharField()
    tempo_alternancia = models.IntegerField()
    tempo_alternancia_pc = models.IntegerField()
    tempo_alternancia_class = models.CharField()
    tempo_inibicao = models.IntegerField()
    tempo_inibicao_pc = models.IntegerField()
    tempo_inibicao_class = models.CharField()
    tempo_flexibilidade = models.IntegerField()
    tempo_flexibilidade_pc = models.IntegerField()
    tempo_flexibilidade_class = models.CharField()
    erro_leitura = models.IntegerField()
    erro_leitura_pc = models.IntegerField()
    erro_leitura_class = models.CharField()
    erro_contagem = models.IntegerField()
    erro_contagem_pc = models.IntegerField()
    erro_contagem_class = models.CharField()
    erro_escolha = models.IntegerField()
    erro_escolha_pc = models.IntegerField()
    erro_escolha_class = models.CharField()
    erro_alternancia = models.IntegerField()
    erro_alternancia_pc = models.IntegerField()
    erro_alternancia_class = models.CharField()

    class Meta:
        managed = False
        db_table = 'fdt_resultados'
