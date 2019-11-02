from decimal import Decimal
from django import forms
from django.core.validators import RegexValidator
from produto.models import Produto, Categoria, SubCategoria
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
        empty_label='--- Selecione uma sub-categoria ---',
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

    def clean_data_cadastro(self):
        data_cadastro = self.cleaned_data.get('data_cadastro')

        if not data_cadastro:
            return data_cadastro

        fim = datetime.now().date()
        inicio = fim - timedelta(days=10)

        if data_cadastro > fim or data_cadastro < inicio:
            raise forms.ValidationError(
                'Deve ser entre ' + inicio.strftime('%d/%m/%Y') + " e " + fim.strftime('%d/%m/%Y'))

        return data_cadastro


class RemoveProdutoForm(forms.Form):
    class Meta:
        fields = ('produto_id')

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=True)

    # <input type="hidden" name="produto_id" id="id_produto_id" value="xxx">
