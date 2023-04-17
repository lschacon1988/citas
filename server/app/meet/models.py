import uuid
from django.db import models
from app.professionals.models import Professionals
from app.users.models import User

from app.services.models import Service

# Create your models here.


class Meet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(null=True,)
    start_time = models.TimeField(null=True,)
    end_time = models.TimeField(null=True,)
    cancelada = models.BooleanField(default=True, blank=True)
    status = models.CharField(max_length=50, choices=[('scheduled', 'Scheduled'), (
        'canceled', 'Canceled'), ('completed', 'Completed')], default='scheduled')    
    professional_attendees = models.ForeignKey(
        Professionals, on_delete=models.CASCADE, name='professional_name', null=True)    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, name='user_name', null=True)    
    name_service = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name_service