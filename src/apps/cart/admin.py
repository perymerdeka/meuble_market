from django.contrib import admin

from apps.cart.models import *

# Register your models here.

class CartModelAdmin(admin.ModelAdmin):
    pass

class CartItemModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(CartModel, CartItemModelAdmin)
admin.site.register(CartItemModel, CartItemModelAdmin)


