from django.db import models

class CorrecaoFDT(models.Model):
    TIPO_CHOICES = [
        ('Tempos', 'Tempos'),
        ('Erros', 'Erros'),
    ]

    FASE_CHOICES = [
        ('Leitura', 'Leitura'),
        ('Contagem', 'Contagem'),
        ('Escolha', 'Escolha'),
        ('Alternância', 'Alternância'),
        ('Inibição', 'Inibição'),
        ('Flexibilidade', 'Flexibilidade'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fase = models.CharField(max_length=20, choices=FASE_CHOICES)
    faixa_etaria_min = models.IntegerField()
    faixa_etaria_max = models.IntegerField()

    media = models.FloatField()
    dp = models.FloatField()
    pc_95 = models.FloatField()
    pc_75 = models.FloatField()
    pc_50 = models.FloatField()
    pc_25 = models.FloatField()
    pc_5 = models.FloatField()

    def __str__(self):
        return f'{self.tipo} - {self.fase} ({self.faixa_etaria_min}–{self.faixa_etaria_max})'
