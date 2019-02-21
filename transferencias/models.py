from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from .helpers import (
    horario_agora_entre_10h_e_16h,
    status_transferencia,
    tipo_transferencia
)


class Transferencia(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    STATUS_CHOICES = (('OK', 'OK'), ('ERRO', 'ERRO'),)

    usuario_id = models.ForeignKey('usuarios.Usuario',
                                   on_delete=models.CASCADE)
    pagador_nome = models.CharField(max_length=128)
    pagador_banco = models.CharField(max_length=3)
    pagador_agencia = models.CharField(max_length=4)
    pagador_conta = models.CharField(max_length=6)
    pagador_conta = models.CharField(max_length=6)
    beneficiario_nome = models.CharField(max_length=128)
    beneficiario_banco = models.CharField(max_length=3)
    beneficiario_agencia = models.CharField(max_length=4)
    beneficiario_conta = models.CharField(max_length=6)
    beneficiario_conta = models.CharField(max_length=6)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    tipo = models.CharField(max_length=4)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} transferiu R$ {} para {}'.format(self.pagador_nome,
                                                    self.valor,
                                                    self.beneficiario_nome)

    def save(self, *args, **kwargs):
        self.status = status_transferencia(self)
        self.tipo = tipo_transferencia(self)
        super(Transferencia, self).save(*args, **kwargs)
