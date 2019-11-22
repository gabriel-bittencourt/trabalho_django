from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    # Página inicial (Todos os produtos)
    path('', views.lista_produtos, name='lista_produtos'),

    path('administrador/', views.administrador, name='administrador'),

    # Página de cadastro de novos itens
    path('cadastrar/', views.cadastrar, name="cadastrar"),

    path('remover/', views.remover, name='remover'),

    path('edita_produto/<int:id>/', views.editar, name='edita_produto'),

    # Página de produtos filtrados por subcategoria
    path('subcategoria/<slug:slug_subcategoria>/', views.lista_produtos,  name='lista_produtos_por_subcategoria'),

    # Página específica de cada produto
    path('<int:id>/<slug:slug_produto>/', views.exibe_produto, name='exibe_produto'),

    # Página de resultados de pesquisa de produtos
    path('pesquisa_produto/', views.pesquisa_produto, name='pesquisa_produto'),
]
