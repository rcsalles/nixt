from django.utils import timezone
from datetime import time
from decimal import Decimal

LIMITE_TED = 5000.00
LIMITE_TRANSFERENCIA = 100000.00


def transferencia_filtro(queryset, filtro):
    data_inicial = filtro.get('data_inicial', None)
    data_final = filtro.get('data_final', None)

    pagador = filtro.get('pagador', None)
    beneficiario = filtro.get('beneficiario', None)

    if data_inicial is not None:
        queryset = queryset.filter(data_criacao__date__gte=data_inicial)

    if data_final is not None:
        queryset = queryset.filter(data_criacao__date__lte=data_final)

    if pagador is not None:
        queryset = queryset.filter(pagador_nome=pagador)

    if beneficiario is not None:
        queryset = queryset.filter(beneficiario_nome=beneficiario)
    return queryset


def transferencia_soma_valores(transferencias):
    total = 0
    for transferencia in transferencias:
        for key, value in transferencia.items():
            if key == 'valor':
                total += Decimal(value)
    return total


def horario_agora_entre_10h_e_16h(horario=None):
    return horario_entre(horario, time(10), time(16))


def horario_entre(horario=None, hora_inicial=time(10), hora_final=time(16)):
    horario = horario or timezone.localtime().time()
    return hora_inicial <= horario <= hora_final


def status_transferencia(transferencia):
    if transferencia.valor > LIMITE_TRANSFERENCIA:
        return 'ERRO'
    return 'OK'


def tipo_transferencia(transferencia):
    tipo = 'DOC'
    if transferencia.pagador_banco == transferencia.beneficiario_banco:
        tipo = 'CC'
    elif horario_agora_entre_10h_e_16h() and transferencia.valor < LIMITE_TED:
        tipo = 'TED'
    return tipo
