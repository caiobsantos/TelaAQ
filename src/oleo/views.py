from django.shortcuts import render

# Create your views here.
from .models import Oleo
from .serializers import OleoSerializer
from rest_framework import generics


class OleoList(generics.ListCreateAPIView):
    queryset = Oleo.objects.all()
    serializer_class = OleoSerializer


class OleoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oleo.objects.all()
    serializer_class = OleoSerializer