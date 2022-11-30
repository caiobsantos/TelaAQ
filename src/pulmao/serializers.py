from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Pulmao

class PulmaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pulmao
        fields = ['id', 'tanque', 'data_analise', 'resultado_cor', 'sensorial', 'brix', 'ph']