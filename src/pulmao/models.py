from django.db import models

# Create your models here.
class Pulmao(models.Model):
    tanque = models.CharField(max_length=50)
    data_analise = models.DateTimeField(auto_now=True)
    resultado_cor = models.CharField(max_length=50, blank=True, null=True)
    sensorial = models.CharField(max_length=100, blank=True, null=True)
    brix = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ph = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)