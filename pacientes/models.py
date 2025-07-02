from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    psicologo = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    escolaridade = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome_completo} ({self.psicologo.username})'
