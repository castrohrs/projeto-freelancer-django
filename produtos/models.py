from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50)


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preço = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
