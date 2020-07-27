from django.db import models
from datetime import datetime

class Grafica(models.Model):
    nome_da_grafica = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=200)
    nome_servicos = models.TextField()
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    data_publicada = models.DateField(default=datetime.now)


class Empresas(models.Model):
    nome_empresa = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=200)
    produtos_aceitos_para_logo = models.TextField()
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    data_publicada = models.DateField(default=datetime.now)