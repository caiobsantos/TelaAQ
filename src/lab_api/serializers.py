from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Decomol

class DecomolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decomol
        fields = ['id', 'data_liberacao', 'resultado_cor', 'sensorial', 'brix', 'ph', 'liberado', 'producao']