from django.db import models

# Create your models here.
class Oleo(models.Model):
    consumo = models.IntegerField()
    data_analise = models.DateField(auto_now=False, auto_now_add=False)