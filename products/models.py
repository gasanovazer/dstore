from django.db import models

from users.models import User

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    descriptions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    catecory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    def __str__(self):
        return f'Продукт: {self.name} | Категории: {self.catecory.name}'

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукты: {self.product.name}'