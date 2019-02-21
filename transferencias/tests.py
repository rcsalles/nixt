from django.test import TestCase
from django.utils.timezone import localtime
from freezegun import freeze_time

from .helpers import horario_agora_entre_10h_e_16h


class HelpersTestCase(TestCase):

    @freeze_time("2019-02-20 18:00:00")  # UTC
    def test_entre_10_e_16_horas_realizado_as_15h(self):
        # aplica -3 horas ('America/Sao_Paulo')
        horario_atual = localtime().time()
        self.assertTrue(horario_agora_entre_10h_e_16h(horario_atual))

    @freeze_time("2019-02-20 20:00:00")  # UTC
    def test_entre_10_e_16_horas_realizado_as_17h(self):
        #  aplica -3 horas ('America/Sao_Paulo')
        horario_atual = localtime().time()
        self.assertFalse(horario_agora_entre_10h_e_16h(horario_atual))

    @freeze_time("2019-02-20 17:00:00")  # UTC
    def test_entre_10_e_16_horas_realizado_sem_parametros_as_14h(self):
        #  aplica -3 horas ('America/Sao_Paulo')
        self.assertTrue(horario_agora_entre_10h_e_16h())


# class TransferenciaModelTestCase(TestCase):

#     def test_save_valor_maior_100_mil_status_ERRO(self):
#         pass

#     def test_save_valor_menor_100_mil_status_OK(self):
#         pass
