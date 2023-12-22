from django.contrib import admin

from apps.cart.models import *

# Register your models here.

class CartModelAdmin(admin.ModelAdmin):
    pass

class CartItemModelAdmin(admin.ModelAdmin):
    pass

class PaymentMethodModelAdmin(admin.ModelAdmin):
    pass

class PaymentMethodTypeModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(CartModel, CartItemModelAdmin)
admin.site.register(CartItemModel, CartItemModelAdmin)
admin.site.register(PaymentMethodModel, PaymentMethodModelAdmin)
admin.site.register(PaymentMethodTypeModel, PaymentMethodTypeModelAdmin)

