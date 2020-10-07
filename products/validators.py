from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def min_0(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is less than zero("0")'),
            params={'value': value},
        )