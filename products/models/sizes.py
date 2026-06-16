from django.db import models
from .products import Product


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
