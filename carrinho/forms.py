from django import forms
from django.core.validators import RegexValidator

from produto.models import Produto, Categoria, SubCategoria
from .models import ItemCarrinho

from trabalho import settings
from datetime import datetime, timedelta


class ItemCarrinhoForm(forms.ModelForm):
    
    class Meta:
        model = ItemCarrinho
        fields = ('qtd', 'produto', 'user')

        produto = forms.IntegerField(widget=forms.HiddenInput(), required=True)

        user = forms.IntegerField(widget=forms.HiddenInput(), required=True)

        qtd = forms.IntegerField(widget=forms.HiddenInput(), required=True)
