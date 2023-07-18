from django.db import models

# Create your models here.
class Configuracao(models.Model):

    setup = models.CharField(max_length=10)
    parametro = models.CharField(max_length=50)
    min_valor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    max_valor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    unidade = models.CharField(max_length=10)