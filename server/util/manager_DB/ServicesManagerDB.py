from app.services.models import Service
from django.core.exceptions import ObjectDoesNotExist

from .BasicManager import BasicManager
class ServicesManagerDB(BasicManager):   
    
    def __init__(self):
        self.__services = Service.objects
    
    def get_by_name(self,name_service):
        try:
            return self.__services.get(name_service__iexact=name_service)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f'El servicio  { name_service} no esta disponible')

  
    
    
   
    