from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Categoria, SubCategoria, Produto
from .forms import ProdutoForm


def lista_produtos(request, slug_subcategoria=None):
    subcategoria = None

    categorias = Categoria.objects.all()

    subcategorias = {}
    produtos = []

    # Carrega as categorias e subcategorias para o menu lateral
    for cat in categorias:
        subcategorias[cat] = []
        for sub in SubCategoria.objects.filter(categoria=cat):
            subcategorias[cat].append(sub)

    # Carrega os produtos (de apenas para uma subcategoria ou de todas subcategoria)
    if slug_subcategoria:
        subcategoria = get_object_or_404(SubCategoria, slug=slug_subcategoria)
        produtos = Produto.objects.filter( subCategoria = subcategoria )
    else:
        produtos = Produto.objects.all()

    print("PRODUTOS", produtos)

    return render(request, 'produto/index.html', {'categorias': categorias,
                                                  'subcategorias': subcategorias,
                                                  'produtos': produtos             })

def exibe_produto(request, id, slug_produto):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produto/exibe.html', {'produto': produto})

def cadastra(request):
    if request.POST:
        
        print("\n\nPOST\n\n")

        produto_id = request.POST.get('produto_id')

        if produto_id:
            produto = get_object_or_404(Produto, pk=produto_id)
            produto_form = ProdutoForm(request.POST, instance=produto)
        else:
            produto_form = ProdutoForm(request.POST)


        if produto_form.is_valid():
            print("\n\nIS VALID\n\n")

            # Atualiza, pois produto já existe
            if produto_id:
                produto = Produto(
                    nome = produto_form.data['nome'],
                    marca = produto_form.data['marca'],
                    preco = produto_form.clean_preco(),
                    subCategoria = get_object_or_404(SubCategoria, id = produto_form.data['subCategoria']),
                    slug = produto_form.data['nome'].lower().replace(' ', '-'),
                    imagem = produto_form.data['nome'].lower().replace(' ', '-') + '.jpg'
                )
                produto.save()

                messages.add_message(request, messages.INFO, 'Produto alterado com sucesso!')

            # Salva novo produto
            else:
                produto = Produto.objects.create(
                    nome = produto_form.data['nome'],
                    marca = produto_form.data['marca'],
                    preco = produto_form.clean_preco(),
                    subCategoria = get_object_or_404(SubCategoria, id = produto_form.data['subCategoria']),
                    slug = produto_form.data['nome'].lower().replace(' ', '-'),
                    imagem = produto_form.data['nome'].lower().replace(' ', '-') + '.jpg'
                )

                messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso!')

            return redirect('produto:exibe_produto', id=produto.id)

        else:
            print("NOT VALID")
            messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo.')
    
    else:
        print("\n\nELSE\n\n")
        produto_form = ProdutoForm()

    # print(type(produto_form))
    return render(request, 'produto/cadastra.html', {'form': produto_form })

# Create your views here.
