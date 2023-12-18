from django.contrib import admin

from apps.users.models import UserModel, RoleModel

# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    pass

class RoleModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserModel, UserModelAdmin)
admin.site.register(RoleModel, RoleModelAdmin)