from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Produto, Fornecedor, Categoria
from .forms import FormularioProduto, FormularioFornecedor, FormularioCategoria

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

def CriarProduto(request):
    form = FormularioProduto()
    if request.method == "POST":
        form = FormularioProduto(request.POST)#recebe os dados enviados
        if form.is_valid():
            produto = Produto(
                nome=form.cleaned_data['nome'],
                codigo=form.cleaned_data['codigo'],
                descricao=form.cleaned_data['descricao'],
                preco=form.cleaned_data['preco'],
                quantEstoque=form.cleaned_data['quantEstoque'],
                data=form.cleaned_data['data'],
                fornecedor=form.cleaned_data['fornecedor'],
            )
            produto.save()
            produto.categoria.set(form.cleaned_data['categories'])
            return HttpResponseRedirect(reverse('index'))
        else:
            form = FormularioProduto(request.POST)

    return render(request, 'criarProduto.html', {'form': form})

def CriarFornecedpor(request):
    formularioFornecedor = FormularioFornecedor()
    if request.method == "POST":
        formularioFornecedor = FormularioFornecedor(request.POST)
    if formularioFornecedor.is_valid():
        supplier = Fornecedor(
            nome = formularioFornecedor.cleaned_data['nome'],
            cnpj = formularioFornecedor.cleaned_data['cnpj'],
            cep = formularioFornecedor.cleaned_data['cep'],
            rua = formularioFornecedor.cleaned_data['rua'],
        )
        supplier.save()
        return HttpResponseRedirect(reverse('index'))
    else: 
        formularioFornecedor = FormularioFornecedor(request.POST)
        formularioFornecedor.errors.clear()

    return render(request, 'criarFornecedor.html', {'formularioFornecedor': formularioFornecedor})

def CriarCategoria(request):
    if request.method == "POST":
        formularioCategoria = FormularioCategoria(request.POST)
        if formularioCategoria.is_valid():
            category = Categoria(
                nome = formularioCategoria.cleaned_data['nome'],
            )
            category.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        formularioCategoria = FormularioCategoria()
        
    return render(request, 'criarCategoria.html', {'formularioCategoria': formularioCategoria})
