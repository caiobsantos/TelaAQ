from rest_framework import serializers
from .models import DecomolHistorico

class DecomolHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecomolHistorico
        fields = ['id', 'data_liberacao', 'resultado_cor', 'sensorial', 'brix', 'ph', 'resultado_analise', 'decomol']