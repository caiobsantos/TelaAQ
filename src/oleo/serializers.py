from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Oleo

class OleoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oleo
        fields = ['id', 'consumo', 'data_analise']