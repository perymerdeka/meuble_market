from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.text import gettext_lazy as _


from apps.users.validator import PostalCodeValidator
from apps.users.manager import UserManager

# Create your models here.
ROLES = [
    ("shop", "shop"),
    ("customer", "customer")
]

class UserModel(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    address = models.TimeField(blank=True, null=True)
    postal_code = models.CharField(validators=[PostalCodeValidator('^[0-9]{6}$', _('Invalid postal code'))], max_length=10, blank=True)
    phone_number = models.CharField(max_length=13)
    role = models.ForeignKey("RoleModel", on_delete=models.SET_NULL, null=True)

    # manager user = dipakai untuk pembuatan akun user
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', "phone_number"]

    def __str__(self) -> str:
        return self.email
    
class RoleModel(models.Model):
    name = models.CharField(max_length=50, choices=ROLES, default=ROLES[1])

    def __str__(self) -> str:
        return self.name
