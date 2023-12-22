from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=4)
    shop = models.ForeignKey("shop.ShopModel", on_delete=models.CASCADE, related_name="products")


class ProductTypeModel(models.Model):
    products = models.ManyToManyField(ProductModel, related_name='product_types')
    name = models.CharField(max_length=50)

class ProductStockModel(models.Model):
    product = models.OneToOneField(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)