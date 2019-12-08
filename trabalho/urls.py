from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produto.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('carrinho/', include('carrinho.urls'))
]
