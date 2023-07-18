from django.shortcuts import render

# Create your views here.
from .models import Configuracao
from .serializers import ConfiguracaoSerializer
from rest_framework import generics


class ConfiguracaoList(generics.ListCreateAPIView):
    queryset = Configuracao.objects.all()
    serializer_class = ConfiguracaoSerializer


class ConfiguracaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Configuracao.objects.all()
    serializer_class = ConfiguracaoSerializer