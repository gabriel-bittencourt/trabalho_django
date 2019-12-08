from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages

from produto.models import Categoria, SubCategoria, Produto
from carrinho.models import ItemCarrinho

from carrinho.forms import *

from functools import reduce


# Exibe página de carrinho
def carrinho(request):

    # Query de itens do carrinho
    itens = ItemCarrinho.objects.filter(user=request.user)

    # Vetor de (produto, qtd, subtotal) no carrinho do usuário atual
    produtos = list(
        ( (i.id, i.produto.subCategoria, i.produto, i.qtd, i.produto.preco * i.qtd) for i in itens )
    )

    # Soma dos subtotais
    if produtos:
        total = reduce(lambda a, b: a+b, list((produto[4] for produto in produtos)))
    else:
        total = 0

    return render(request, 'carrinho/carrinho.html', {"total": total, "produtos": produtos})

# Remove do carrinho
def remover_do_carrinho(request):
    if request.POST:
        item_id = request.POST.get('item_id')

        item = get_object_or_404(ItemCarrinho, id=item_id)

        item.delete()

        return render(request, 'carrinho/carrinho.html')

# Adiciona ao carrinho
def adicionar_ao_carrinho(request):
    if request.POST:

        produto_id = request.POST.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)
        qtd = 1


        # Verifica se item já está no carrinho do usuário

        # Se já estiver, adiciona mais um ao carrinho
        try:
            itemCarrinho = ItemCarrinho.objects.get(produto=produto, user=request.user)

            itemCarrinho.qtd = itemCarrinho.qtd + 1

            itemCarrinho.save()


        # Se não estiver salva novo item de carrinho
        except ItemCarrinho.DoesNotExist:
            itemCarrinho = ItemCarrinho(
                produto=produto, user=request.user, qtd=qtd)

            itemCarrinho.save()

        return render(request, 'produto/index.html')
