from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=200, unique=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantEstoque = models.IntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome