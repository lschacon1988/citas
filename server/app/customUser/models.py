import uuid 
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    tlf = models.CharField(max_length=45, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.username
    

