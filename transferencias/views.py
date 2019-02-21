from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Transferencia
from .serializers import TransferenciaSerializer
from .helpers import transferencia_filtro, transferencia_soma_valores


class ListTransferencia(generics.ListCreateAPIView):
    """
    get:
        Lista transferências

        Filtros disponíveis enviados por query_string; Todos os valores são
        opcionais e quando informados são aplicados ao filtro

        /transferências/?data_inicio=2019-02-20&data_final=2019-02-25&pagador=RafaelSalles&beneficiario=Rafael

        @data_inicio : data de inicio no formato YYYY-MM-DD
        @data_final  : data final no formato YYYY-MM-DD
        @pagador     : Nome do pagador
        @beneficiario: Nome do beneficiário

    post:
        Cria Transferência
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = TransferenciaSerializer

    def get_queryset(self):
        queryset = Transferencia.objects.all()
        queryset = transferencia_filtro(queryset, self.request.query_params)
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        transferencias = response.data['results']
        response.data['somatorio'] = transferencia_soma_valores(transferencias)
        return response


class DetailTransferencia(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
        Detalhes de uma transferência
    delete:
        Exclui uma transferência
    put:
        Atualiza uma transferência
    patch:
        Atualiza um ou mais campos da transferência
    """
    permission_classes = (IsAuthenticated,)
    queryset = Transferencia.objects.all()
    serializer_class = TransferenciaSerializer
