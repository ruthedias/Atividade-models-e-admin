from django.shortcuts import render
from .models import Produto, Fornecedor, Categoria

# Create your views here.

def produto(request):
    produtos = Produto.objects.all()
    fornecedores = Fornecedor.objects.all()
    categorias = Categoria.objects.all()
    context = {'produtos': produtos, 'fornecedores': fornecedores, 'categorias': categorias}
    return render(request, 'produtos.html', context)

def detalhes(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'detalhes.html', {'produto': produto})
