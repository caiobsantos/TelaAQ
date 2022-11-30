from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import PulmaoHistorico

class PulmaoHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PulmaoHistorico
        fields = ['id', 'tanque', 'data_analise', 'resultado_cor', 'sensorial', 'brix', 'ph']