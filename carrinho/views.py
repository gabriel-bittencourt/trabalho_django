from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages

from produto.models import Categoria, SubCategoria, Produto
from carrinho.models import ItemCarrinho

from carrinho.forms import *

from .carrinho import Carrinho

from functools import reduce


# Exibe página de carrinho
def carrinho(request):

    carrinho = Carrinho(request)

    # Se tem um usuário logado, carrega do banco
    if request.user.is_authenticated:
        itens = ItemCarrinho.objects.filter(user=request.user)

    # Se não, carrega da sessão
    else:
        itens = carrinho.get_produtos()


    # Vetor de (produto, qtd, subtotal)
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
        produto_id = request.POST.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)

        # Se usuário estiver logado, remove do banco
        if request.user.is_authenticated:
            item = get_object_or_404(ItemCarrinho, produto=produto, user=request.user)
            item.delete()
        
        #
        else:
            carrinho = Carrinho(request)
            carrinho.remover(produto_id)

        return render(request, 'carrinho/carrinho.html')

# Adiciona ao carrinho
def adicionar_ao_carrinho(request):
    if request.POST:

        produto_id = request.POST.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)
        qtd = 1

        # Se usuário estiver logado
        if request.user.is_authenticated:

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

        # Se usuário não estiver logado
        else:
            carrinho = Carrinho(request)
            carrinho.adicionar(produto_id, qtd)

            print(carrinho.carrinho)
            

        return render(request, 'produto/index.html')


def atualizar_quantidade(request, adicionar=True):
    if request.POST:
        
        produto_id = request.POST.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)


        adicionar = request.POST.get('adicionar') == "True"

        # Se usuário estiver logado, atualiza no banco
        if request.user.is_authenticated:
            item = get_object_or_404(ItemCarrinho, produto=produto, user=request.user)
            
            if adicionar:
                item.qtd += 1
                item.save()
            else:
                if item.qtd == 1:
                    remover_do_carrinho(request)
                else:
                    item.qtd -= 1
                    item.save()

        #
        else:
            carrinho = Carrinho(request)

            if adicionar:
                carrinho.adicionar(produto_id, 1)
            else:
                carrinho.retirar(produto_id)


        return render(request, 'carrinho/carrinho.html')