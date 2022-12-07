from rest_framework import serializers
from .models import TrocaHistorico

class DecomolTrocaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrocaHistorico
        fields = ['id', 'data_troca', 'decomol_troca', 'data_fim']