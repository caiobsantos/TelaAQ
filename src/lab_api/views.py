from django.shortcuts import render

# Create your views here.
from .models import Decomol
from .serializers import DecomolSerializer
from rest_framework import generics


class DecomolList(generics.ListCreateAPIView):
    queryset = Decomol.objects.all()
    serializer_class = DecomolSerializer


class DecomolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Decomol.objects.all()
    serializer_class = DecomolSerializer