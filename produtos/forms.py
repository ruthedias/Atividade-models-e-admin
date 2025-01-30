from django import forms
from .models import Categoria, Fornecedor

class ProductForm(forms.Form):
    nome = forms.CharField(label="Nome")
    codigo = forms.CharField(label="Código")
    descricao = forms.CharField(label="Descrição", widget=forms.Textarea)
    preco = forms.DecimalField(label="Preço")
    quantEstoque = forms.IntegerField(label="Quantidade em Estoque")
    data = forms.DateField(label="Data", widget=forms.DateInput(attrs={'type': 'date'}))
    categories = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all(), widget=forms.CheckboxSelectMultiple, label="Categorias")
    fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all(), label="Fornecedor")


class SupplierForm(forms.Form):
    nome = forms.CharField(label="Nome")
    cnpj = forms.CharField(label="CNPJ")
    cep = forms.CharField(label="Cep")
    rua = forms.CharField(label="Endereço")

class CategoryForm(forms.Form):
    nome = forms.CharField(label="Categoria")