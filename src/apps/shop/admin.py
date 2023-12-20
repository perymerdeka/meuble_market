from django.contrib import admin

from apps.shop.models import ShopModel

# Register your models here.
class ShopModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShopModel, ShopModelAdmin)