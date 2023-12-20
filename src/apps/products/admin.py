from django.contrib import admin

from apps.products.models import *

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    pass

class ProductTypeModelAdmin(admin.ModelAdmin):
    pass

class ProductStockModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(ProductTypeModel, ProductTypeModelAdmin)
admin.site.register(ProductStockModel, ProductStockModelAdmin)
