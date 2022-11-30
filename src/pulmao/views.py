from django.shortcuts import render

# Create your views here.
from .models import Pulmao
from .serializers import PulmaoSerializer
from rest_framework import generics


class PulmaoList(generics.ListCreateAPIView):
    queryset = Pulmao.objects.all()
    serializer_class = PulmaoSerializer


class PulmaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pulmao.objects.all()
    serializer_class = PulmaoSerializer