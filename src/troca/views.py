from django.shortcuts import render
from .models import TrocaHistorico
from .serializers import DecomolTrocaSerializer
from rest_framework import generics

class DecomolTrocaList(generics.ListCreateAPIView):
    queryset = TrocaHistorico.objects.all()
    serializer_class = DecomolTrocaSerializer


class DecomolTrocaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrocaHistorico.objects.all()
    serializer_class = DecomolTrocaSerializer