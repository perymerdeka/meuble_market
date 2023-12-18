from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class PostalCodeValidator(RegexValidator):
    regex = r'^[A-Za-z0-9]{5,10}$'
    message = _('Enter a valid postal code. It should be between 5 and 10 characters and can include letters and numbers.')
    flags = 0