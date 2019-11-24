from decimal import Decimal
from django import forms
from django.core.validators import RegexValidator
from produto.models import Produto, Categoria, SubCategoria, ItemCarrinho
from trabalho import settings
from datetime import datetime, timedelta


class PesquisaProdutoForm(forms.Form):
    class Meta:
        fields = ('busca_por')

    busca_por = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm w-75 mr-2',
                'placeholder': 'Pesquisa',
                'maxlength': '120',
                'autocomplete': 'off'
            }
        ),
        required=False)


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('produto_id', 'subCategoria', 'nome', 'marca', 'preco')

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    subCategoria = forms.ModelChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        queryset=SubCategoria.objects.all().order_by('nome'),
        empty_label='--- Selecione uma Categoria ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    nome = forms.CharField(
        error_messages={'required': 'Campo obrigatório.',
                        'unique': 'Produto duplicado.'},
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)

    marca = forms.CharField(
        error_messages={'required': 'Campo obrigatório.'},
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-sm', 'maxlength': '50'}),
        required=True)

    preco = forms.CharField(
        localize=True,
        error_messages={'required': 'Campo obrigatório.', },
        validators=[RegexValidator(
            regex='^[0-9]{1,7}(,[0-9]{2})?$', message="Informe o valor no formato 9999999,99.")],
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                      'maxlength': '10',
                                      'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'}),
        required=True)

    def clean_preco(self):
        preco = self.data['preco']

        if not preco:
            return preco

        preco = Decimal(preco.replace(',', '.'))

        return preco


class RemoveProdutoForm(forms.Form):
    class Meta:
        fields = ('produto_id')

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=True)


class ItemCarrinhoForm(forms.ModelForm):
    
    class Meta:
        model = ItemCarrinho
        fields = ('qtd', 'produto', 'user')

        produto = forms.IntegerField(widget=forms.HiddenInput(), required=True)

        user = forms.IntegerField(widget=forms.HiddenInput(), required=True)

        qtd = forms.IntegerField(widget=forms.HiddenInput(), required=True)
