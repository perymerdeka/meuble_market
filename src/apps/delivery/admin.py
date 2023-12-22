from django.contrib import admin

from apps.delivery.models import DeliveryModel

# Register your models here.

class DeliveryModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(DeliveryModel, DeliveryModelAdmin)