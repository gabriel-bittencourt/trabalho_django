from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),

    path('<slug:slug_categoria>/', views.lista_produtos,  name='lista_produtos_por_categoria'),

    path('<int:id>/<slug:slug_produto>/', views.exibe_produto, name='exibe_produto'),
]
