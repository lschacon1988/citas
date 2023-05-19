import uuid
from django.db import models


# Create your models here.
class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    name_service = models.CharField(max_length=150, unique=True)
    duration = models.DurationField()
    
    objects = models.Manager()
    