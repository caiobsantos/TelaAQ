from django.db import models

# Create your models here.
class TrocaHistorico(models.Model):
    decomol_troca = models.CharField(max_length=50)
    data_troca = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(auto_now=True, null=True)