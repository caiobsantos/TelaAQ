from django.db import models

# Create your models here.
class Oleo(models.Model):
    consumo = models.IntegerField()
    data_analise = models.DateTimeField(auto_now=True)