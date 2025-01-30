from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Produto, Fornecedor, Categoria
from .forms import ProductForm, SupplierForm, CategoryForm
from datetime import datetime

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


def createProduto(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)#recebe os dados enviados
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
            produto.categories.set(form.cleaned_data['categories'])
            return HttpResponseRedirect(reverse('index'))
        else:
            form = ProductForm(request.POST)

    return render(request, 'createProduto.html', {'form': form})

def CreateSupplier(request):
    formSupplier = SupplierForm()
    if request.method == "POST":
        formSupplier = SupplierForm(request.POST)
    if formSupplier.is_valid():
        supplier = Fornecedor(
            nome = formSupplier.cleaned_data['nome'],
            cnpj = formSupplier.cleaned_data['cnpj'],
            cep = formSupplier.cleaned_data['cep'],
            rua = formSupplier.cleaned_data['rua'],
        )
        supplier.save()
        return HttpResponseRedirect(reverse('index'))
    else: 
        formSupplier = SupplierForm(request.POST)
        formSupplier.errors.clear()

    return render(request, 'createSupplier.html', {'formSupplier': formSupplier})

def CreateCategory(request):
    if request.method == "POST":
        formCategory = CategoryForm(request.POST)
        if formCategory.is_valid():
            category = Categoria(
                nome = formCategory.cleaned_data['nome'],
            )
            category.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        formCategory = CategoryForm()
        
    return render(request, 'createCategory.html', {'formCategory': formCategory})