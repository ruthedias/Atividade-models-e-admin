from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14, unique=True)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=200, unique=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantEstoque = models.IntegerField()
    data = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Categoria)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome



