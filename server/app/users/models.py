# import uuid
# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save

# # Create your models here.


# class UserProfile(models.Model):
#     user = models.OneToOneField(User,  on_delete=models.CASCADE)
#     tlf = models.CharField(max_length=90, unique=True, null=True, blank=True)
    
    
#     def __str__(self):
#         return  self.user.username
    
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# def save_user_profile(sender,instance,**kwargs):
#     instance.userprofile.save()

# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)


import uuid 
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Client(AbstractUser):
    # add additional fields in here   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    tlf = models.CharField(max_length=45, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.username
    