from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Usuario
from .serializers import UsuarioSerializer


class ListUsuario(generics.ListCreateAPIView):
    """
    get:
        Lista usuários
    post:
        Cria usuário
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class DetailUsuario(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
        Detalhes de uma usuário
    delete:
        Exclui uma usuário
    put:
        Atualiza uma usuário
    patch:
        Atualiza um ou mais campos da usuário
    """
    permission_classes = (IsAuthenticated,)
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
