from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    nome = models.CharField(null=False)
    descricao = models.CharField(null=False)
    valor = models.IntegerField(null=False)