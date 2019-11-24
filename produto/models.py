from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        db_table='categoria'

    def get_absolute_path(self):
        return reverse('produto:lista_produtos_por_categoria', args=[self.slug])

    def __str__(self):
        return self.nome


 # Create your models here.
class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        db_table='subCategoria'

    def get_absolute_path(self):
        return reverse('produto:lista_produtos_por_subcategoria', args=[self.slug])

    def __str__(self):
        return self.nome


class Produto(models.Model):
    subCategoria = models.ForeignKey(SubCategoria, related_name='produtos', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200, db_index=True)
    marca = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    class Meta:
        db_table = 'produto'

    def get_absolute_path(self):
        return reverse('produto:exibe_produto', args=[self.id, self.slug])
        
    def __str__(self):
        return self.nome


class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, related_name='produtos', on_delete=models.DO_NOTHING)
    qtd = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='produtos',
                             on_delete=models.DO_NOTHING,
                             null=True)

    class Meta:
        db_table = 'item_carrinho'
        ordering = ('user',)

    def __str__(self):
        return "USER: " + str(self.user) + ", PRODUTO: " + str(self.produto)
