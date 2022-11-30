from django.shortcuts import render

# Create your views here.
from .models import PulmaoHistorico
from .serializers import PulmaoHistoricoSerializer
from rest_framework import generics


class PulmaoHistoricoList(generics.ListCreateAPIView):
    queryset = PulmaoHistorico.objects.all()
    serializer_class = PulmaoHistoricoSerializer


class PulmaoHistoricoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PulmaoHistorico.objects.all()
    serializer_class = PulmaoHistoricoSerializer