from rest_framework import serializers
from .models import Configuracao

class ConfiguracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracao
        fields = ['setup', 'parametro', 'min_valor', 'max_valor', 'unidade']