import uuid
from django.db import models
from app.professionals.models import Professionals
from app.users.models import User

from app.services.models import Service

# Create your models here.

class Meet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    date = models.DateField(null=True,)
    hour= models.TimeField(null=True,)
    cancelada = models.BooleanField(default=True,blank=True)
    professional_id = models.ForeignKey(Professionals, on_delete=models.CASCADE, name='professional_id',null=True)   
    professionals_name = models.CharField(max_length=250, blank=True,null=True) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,name='user_id',null=True)
    user_name = models.CharField(max_length=250, blank=True,null=True) 
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE,name='service_id',null=True)