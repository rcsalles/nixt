from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
