from decimal import Decimal
from trabalho import settings

from produto.models import Produto
from carrinho.models import ItemCarrinho

class Carrinho(object):

    # Inicializa um objeto Carrinho
    def __init__(self, request):
        self.session = request.session

        self.carrinho = self.session.get(settings.CARRINHO_SESSION_ID)

        # Se a sessão não tiver um carrinho
        if not self.carrinho:
            self.carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}


    # Retorna a quantidade de itens no carrinho
    def __len__(self):
        return sum(item['qtd'] for item in self.carrinho.values())

    # Retorna os items do carrinho da sessão atual
    def get_produtos(self):

        lista = []

        for item in self.carrinho.values():
            produto = Produto.objects.get(id=item['id'])

            # Cria novo item de carrinho local (Não salva no banco)
            itemCarrinho = ItemCarrinho(
                    produto=produto, user=None, qtd=item['qtd'])

            lista.append(itemCarrinho)
        
        return lista

    # Adiciona um novo item ao carrinho
    def adicionar(self, id, qtd):
        produto = Produto.objects.get(id=id)

        if id not in self.carrinho:
            self.carrinho[id] = {'id': id, 'preco': str(produto.preco), 'qtd': qtd}
        else:
            self.carrinho[id]['qtd'] += qtd

        self.salvar()        


    def alterar(self, id, quantidade):
        self.carrinho[id]['quantidade'] = quantidade
        self.salvar()

    # Remove do carrinho
    def remover(self, id):

        if id in self.carrinho:
            del self.carrinho[id]
            self.salvar()   

    # Salva as modificaões
    def salvar(self):
        self.session.modified = True

    # Limpa o carrinho
    def limpar(self):
        self.session[settings.CARRINHO_SESSION_ID] = {}

    # Retorna o valor total
    def get_total(self):
        return sum(Decimal(item['preco']) * item['qtd'] for item in self.carrinho.values())
