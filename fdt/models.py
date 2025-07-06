from django.db import models
from django.contrib.auth.models import User
from pacientes.models import Paciente # Importa o modelo Paciente
from django.utils import timezone


class FdtResultados(models.Model):
    id_resultado = models.AutoField(primary_key=True)
    id_psicologo = models.IntegerField()
    id_paciente = models.IntegerField()
    data_resultado = models.DateTimeField()
    tempo_leitura = models.IntegerField()
    tempo_leitura_pc = models.IntegerField()
    tempo_leitura_class = models.CharField(max_length=50)
    tempo_contagem = models.IntegerField()
    tempo_contagem_pc = models.IntegerField()
    tempo_contagem_class = models.CharField(max_length=50)
    tempo_escolha = models.IntegerField()
    tempo_escolha_pc = models.IntegerField()
    tempo_escolha_class = models.CharField(max_length=50)
    tempo_alternancia = models.IntegerField()
    tempo_alternancia_pc = models.IntegerField()
    tempo_alternancia_class = models.CharField(max_length=50)
    tempo_inibicao = models.IntegerField()
    tempo_inibicao_pc = models.IntegerField()
    tempo_inibicao_class = models.CharField(max_length=50)
    tempo_flexibilidade = models.IntegerField()
    tempo_flexibilidade_pc = models.IntegerField()
    tempo_flexibilidade_class = models.CharField(max_length=50)
    erro_leitura = models.IntegerField()
    erro_leitura_pc = models.IntegerField()
    erro_leitura_class = models.CharField(max_length=50)
    erro_contagem = models.IntegerField()
    erro_contagem_pc = models.IntegerField()
    erro_contagem_class = models.CharField(max_length=50)
    erro_escolha = models.IntegerField()
    erro_escolha_pc = models.IntegerField()
    erro_escolha_class = models.CharField(max_length=50)
    erro_alternancia = models.IntegerField()
    erro_alternancia_pc = models.IntegerField()
    erro_alternancia_class = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fdt_resultados'


class FdtReferencia(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    fase = models.CharField(max_length=50)
    faixa_etaria_min = models.IntegerField()
    faixa_etaria_max = models.IntegerField()
    media = models.FloatField()
    dp = models.FloatField()
    pc_95 = models.FloatField()
    pc_75 = models.FloatField()
    pc_50 = models.FloatField()
    pc_25 = models.FloatField()
    pc_5 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'fdt_referencia'
