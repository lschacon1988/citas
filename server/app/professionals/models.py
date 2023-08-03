import uuid
from django.db import models
from django.utils import timezone
from app.customUser.models import CustomUser

# Create your models here.


class Professionals(models.Model):
    id = models.UUIDField( primary_key=True,default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='professionals', null=True, blank=True)
    specialty = models.CharField(max_length=150)    
    admission_date = models.DateField(null=True, auto_now=True)
    activity = models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return self.user.first_name + ' ' + self.user.last_name
