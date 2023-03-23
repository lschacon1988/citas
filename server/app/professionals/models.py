import uuid
from django.db import models
from django.utils import timezone

# Create your models here.


class Professionals(models.Model):
    id = models.UUIDField( primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    specialty = models.CharField(max_length=150)
    tlf = models.CharField(max_length=200, unique=True, default='')
    admission_date = models.DateField(null=True, auto_now=True)
