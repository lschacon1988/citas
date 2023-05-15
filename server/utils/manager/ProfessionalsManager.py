
from django.db import models

class ProfessionalManager(models.Manager):
    def professional(self, name):
        return super().get_queryset().filter(name=name)