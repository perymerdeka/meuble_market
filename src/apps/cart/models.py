from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your models here.
class CartModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    items = models.ManyToManyField('products.ProductModel', through='CartItemModel')
    payment = models.OneToOneField("PaymentMethodModel", on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart for {self.user.first_name}"

class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    product = models.ForeignKey('products.ProductModel', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart.user.first_name}'s cart"
    
class PaymentMethodModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=13,)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    payment_type = models.OneToOneField("PaymentMethodTypeModel", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class PaymentMethodTypeModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
