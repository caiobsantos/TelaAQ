from django.shortcuts import render

# Create your views here.
from .models import DecomolHistorico
from .serializers import  DecomolHistoricoSerializer
from rest_framework import generics


class DecomolHistoricoList(generics.ListCreateAPIView):
    queryset = DecomolHistorico.objects.all()
    serializer_class = DecomolHistoricoSerializer


class DecomolHistoricoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DecomolHistorico.objects.all()
    serializer_class = DecomolHistoricoSerializer