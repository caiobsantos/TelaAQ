from django.db import models

# Create your models here.
class PulmaoHistorico(models.Model):
    tanque = models.CharField(max_length=50)
    data_analise = models.DateTimeField(auto_now_add=True)
    resultado_cor = models.CharField(max_length=50)
    sensorial = models.CharField(max_length=100)
    brix = models.DecimalField(max_digits=5, decimal_places=2)
    ph = models.DecimalField(max_digits=4, decimal_places=2)