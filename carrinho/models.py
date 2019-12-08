from django.db import models
from django.urls import reverse
from django.conf import settings

from produto.models import Produto

class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, related_name='produtos', on_delete=models.DO_NOTHING)
    qtd = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='users',
                             on_delete=models.DO_NOTHING,
                             null=True)

    class Meta:
        db_table = 'item_carrinho'
        ordering = ('user',)

    def __str__(self):
        return "USER: " + str(self.user) + ", PRODUTO: " + str(self.produto) + ", QTD: " + str(self.qtd)
