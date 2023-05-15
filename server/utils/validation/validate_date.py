from datetime import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_date( date):
    
    if date < timezone.now():
        raise ValidationError(
            _('La fecha debe ser en el futuro.'),
            params={'date': date},
        )