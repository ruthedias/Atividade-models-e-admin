from django.contrib import admin
from .models import Produto, Fornecedor, Categoria

# Register your models here.
class adminProduto(admin.ModelAdmin):
    list_display=('codigo', 'nome', 'preco', 'quantEstoque', 'data')
    search_fields=('codigo', 'nome')
    list_filter=('data',)
    ordering=('-data',)

admin.site.register(Produto, adminProduto)
admin.site.register(Fornecedor)
admin.site.register(Categoria)


