from django.shortcuts import render, get_object_or_404
from .models import Categoria, SubCategoria, Produto

def lista_produtos(request, slug_categoria=None, slug_subcategoria=None):
    categoria = subcategoria = None

    categorias = Categoria.objects.all()

    subcategorias = {}
    produtos = {}

    for cat in categorias:
        subcategorias[cat] = []
        for sub in SubCategoria.objects.filter(categoria=cat):
            subcategorias[cat].append(sub)
            produtos[sub] = Produto.objects.filter(subCategoria=sub)

    if slug_categoria:
        produtos = {}
        cat = get_object_or_404(Categoria, slug = slug_categoria)
        subs = SubCategoria.objects.filter(categoria=cat)
        for sub in subs:
            produtos[sub] = Produto.objects.filter(subCategoria=sub)

    return render(request, 'produto/index.html', {'categorias': categorias,
                                                  'subcategorias': subcategorias,
                                                  'produtos': produtos             })

def exibe_produto(request, id, slug_produto):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produto/exibe.html', {'produto': produto})

# Create your views here.
