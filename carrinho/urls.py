from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    # Adicionar item ao carrinho
    path('adicionar_ao_carrinho', views.adicionar_ao_carrinho, name="adicionar_ao_carrinho"),

    # Remover item do carrinho
    path('remover_do_carrinho', views.remover_do_carrinho, name="remover_do_carrinho"),

    # Página do carrinho atual
    path('', views.carrinho, name="carrinho"),
]
