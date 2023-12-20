from django.db import models

# Create your models here.
class ShopModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=13)
    images = models.ImageField(upload_to="shop_images/")
    fax = models.CharField(max_length=60)
    geolocation = models.CharField(max_length=200)
    owner = models.ForeignKey("users.UserModel", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
