from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Categoria, SubCategoria, Produto
from .forms import ProdutoForm, PesquisaProdutoForm


def lista_produtos(request, slug_subcategoria=None):
    subcategoria = None

    categorias = Categoria.objects.all()

    subcategorias = {}
    lista_produtos = []
    produtos_subcategorias = []

    # Carrega as categorias e subcategorias para o menu lateral
    for cat in categorias:
        subcategorias[cat] = []
        for sub in SubCategoria.objects.filter(categoria=cat):
            subcategorias[cat].append(sub)

    # Carrega itens da pesquisa
    form = PesquisaProdutoForm(request.GET)
    if form.is_valid():
        busca_por = form.cleaned_data['busca_por']

        # Filtra produtos pelo nome
        lista_produtos = Produto.objects.filter(
            nome__icontains=busca_por).order_by('nome')

        if len(lista_produtos) == 0:
            messages.add_message(request, messages.INFO, 'Nenhum produto encontrado.')

        # Cria tuplas (Produto, Subcategoria)
        for produto in lista_produtos:
            subcategoria = get_object_or_404(
                SubCategoria, id=produto.subCategoria.id
            )
            produtos_subcategorias.append(
                (produto, subcategoria)
            )

        # Carrega os produtos de apenas para uma subcategoria
        if slug_subcategoria:
            produtos_subcategorias = []

            subcategoria = get_object_or_404(
                SubCategoria, slug=slug_subcategoria)
            lista_produtos = Produto.objects.filter(subCategoria=subcategoria)

            # Cria tuplas (Produto, Subcategoria)
            for produto in lista_produtos:
                produtos_subcategorias.append((produto, subcategoria))

    # Páginas de 6 itens
    paginator = Paginator(produtos_subcategorias, 6)

    # Parâmetro que será utilizado para selecionar a página a ser exibida
    pagina = request.GET.get('page')

    # Carrega os itens da página atual
    produtos = paginator.get_page(pagina)

    return render(request, 'produto/index.html', {'categorias': categorias,
                                                  'subcategorias': subcategorias,
                                                  'produtos': produtos,
                                                  'form': form})


def exibe_produto(request, id, slug_produto):
    # Form que será utilizado na barra de busca
    form = PesquisaProdutoForm(request.GET)

    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produto/exibe.html', {'produto': produto,
                                                  'form': form})


def pesquisa_produto(request):
    form = PesquisaProdutoForm()
    return render(request, 'produto/pesquisa_produto.html', {
        'form': form
    })


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
                    nome=produto_form.data['nome'],
                    marca=produto_form.data['marca'],
                    preco=produto_form.clean_preco(),
                    subCategoria=get_object_or_404(
                        SubCategoria, id=produto_form.data['subCategoria']),
                    slug=produto_form.data['nome'].lower().replace(' ', '-'),
                    imagem=produto_form.data['nome'].lower().replace(
                        ' ', '-') + '.jpg'
                )
                produto.save()

                messages.add_message(request, messages.INFO,
                                     'Produto alterado com sucesso!')

            # Salva novo produto
            else:
                produto = Produto.objects.create(
                    nome=produto_form.data['nome'],
                    marca=produto_form.data['marca'],
                    preco=produto_form.clean_preco(),
                    subCategoria=get_object_or_404(
                        SubCategoria, id=produto_form.data['subCategoria']),
                    slug=produto_form.data['nome'].lower().replace(' ', '-'),
                    imagem=produto_form.data['nome'].lower().replace(
                        ' ', '-') + '.jpg'
                )

                messages.add_message(request, messages.INFO,
                                     'Produto cadastrado com sucesso!')

            return redirect('produto:exibe_produto', id=produto.id)

        else:
            print("NOT VALID")
            messages.add_message(request, messages.ERROR,
                                 'Corrija o(s) erro(s) abaixo.')

    else:
        print("\n\nELSE\n\n")
        produto_form = ProdutoForm()

    # print(type(produto_form))
    return render(request, 'produto/cadastra.html', {'form': produto_form})
