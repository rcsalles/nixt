from rest_framework import serializers
from .models import Transferencia


class TransferenciaSerializer(serializers.ModelSerializer):

    class Meta:
        read_only_fields = ('status', 'tipo', )
        exclude = ('deleted',)
        model = Transferencia
