from django.contrib.auth.models import User, Group
from rest_framework import serializers, fields
from .models import Oleo

class OleoSerializer(serializers.ModelSerializer):
    data_analise = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = Oleo
        fields = ['id', 'consumo', 'data_analise']