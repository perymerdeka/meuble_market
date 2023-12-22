from django.db import models


class DeliveryModel(models.Model):
    user = models.ForeignKey("users.UserModel", on_delete=models.CASCADE)
    product = models.ForeignKey("products.ProductModel", on_delete=models.CASCADE)
    address = models.TextField()
    scheduled_delivery_datetime = models.DateTimeField()
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Delivery of {self.product.name} for {self.user.first_name} at {self.address}"
