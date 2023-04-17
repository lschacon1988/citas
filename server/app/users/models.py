import uuid
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, default='')
    lastname = models.CharField(max_length=150, default='')
    email = models.EmailField(unique=True, default='')
    tlf = models.CharField(max_length=250, unique=True, default='')
    password = models.CharField(max_length=250, default='')
    
    def __str__(self):
        return  self.name
