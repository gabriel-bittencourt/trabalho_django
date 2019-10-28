from decimal import Decimal
from django import forms
from django.core.validators import RegexValidator
from produto.models import Produto, Categoria, SubCategoria
from trabalho import settings
from datetime import datetime, timedelta

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('produto_id', 'subCategoria', 'nome', 'marca', 'preco')

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    # <input type="hidden" name="produto_id" id="id_produto_id" value="xxx">

    subCategoria = forms.ModelChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        queryset=SubCategoria.objects.all().order_by('nome'),
        empty_label='--- Selecione uma sub-categoria ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    #      {{ form.categoria }}
    #      <select name="categoria" class="form-control form-control-sm" required id="id_categoria">
    #          <option value="" selected>--- Selecione um(a) categoria ---</option>
    #          <option value="1">Categoria 1</option>
    #          <option value="2">Categoria 2</option>
    #          <option value="3">Categoria 3</option>
    #      </select>

    nome = forms.CharField(
        error_messages={'required': 'Campo obrigatório.',
                        'unique': 'Produto duplicado.'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)

    marca = forms.CharField(
        error_messages={'required': 'Campo obrigatório.'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '50'}),
        required=True)

    # <input type="text"
    #        name="nome"
    #        id="id_nome"
    #        class="form-control form-control-sm"
    #        maxlength="120"
    #        required>

    preco = forms.CharField(
        localize=True,
        error_messages={'required': 'Campo obrigatório.', },
        validators=[RegexValidator(regex='^[0-9]{1,7}(,[0-9]{2})?$', message="Informe o valor no formato 9999999,99.")],
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                      'maxlength': '10',
                                      'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'}),
        required=True)

    # <input type="text"
    #        name="preco"
    #        id="id_preco"
    #        class="form-control form-control-sm"
    #        maxlength="10"
    #        onkeypress="return (event.charCode >= 48 &amp;&amp; event.charCode <= 57) || event.charCode == 44"
    #        required="">

    # <input type='text'
    #        name='data_cadastro'
    #        class='form-control form-control-sm'
    #        required=''
    #        id='id_data_cadastro'
    #        maxlength='10'>

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
