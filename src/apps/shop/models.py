from django.db import models
from django.core.exceptions import PermissionDenied




# Create your models here.
class ShopModel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=13)
    owner = models.ForeignKey("users.UserModel", on_delete=models.CASCADE, related_name="shop_model", null=True)

    # buat authentikasi sederhana supaya yang bisa edit hanya owner nya
    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user making the modification
        print(self.owner)


        if self.owner and self.owner != user:
            raise PermissionDenied("You do not have permission to edit this shop.")

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name