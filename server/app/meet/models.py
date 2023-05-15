import uuid
from django.db import models
from app.professionals.models import Professionals
from app.customUser.models import CustomUser


from app.services.models import Service
# from utils.manager.ProfessionalsManager import ProfessionalManager
# from utils.validation.future_date_validator import validate_date
from datetime import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
        
def future_date_validator( date):
            
    if date < timezone.now().date():
        raise ValidationError(
                    _('La fecha debe ser en el futuro.'),
                    params={'date': date},)
class Meet(models.Model):   
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(null=True, validators=[future_date_validator])
    start_time = models.TimeField(null=True,)
    end_time = models.TimeField(null=True,)
    cancelada = models.BooleanField(default=True, blank=True)
    status = models.CharField(max_length=50, choices=[('scheduled', 'Scheduled'), (
        'canceled', 'Canceled'), ('completed', 'Completed')], default='scheduled')    
    professional_attendees = models.ForeignKey(
        Professionals, on_delete=models.CASCADE, name='professional_name', null=True)    
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, name='user_name', null=True)    
    name_service = models.CharField(max_length=50, default= 'Tradicional')
    objects = models.Manager()
    # professional_manager = ProfessionalManager()

    
