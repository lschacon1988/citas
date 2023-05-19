from abc import ABC, abstractmethod
from django.core.exceptions import ObjectDoesNotExist


class BasicManager(ABC):    
    
    # con @abstractmethod se obliga a las clases hijas a implementar los metodos
    # que se definen en la clase padre
    def __init__(self, model):
        self.model = model.objects
    
    def get_by_name(self):
        pass
   
    
    def get_all(self):
        pass
    
    
    def get_by_id(self, object_id):
        
        try:
            return self.model.get(id = object_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f'El profesional {object_id} no esta disponible')
        
    
    
    def create(self):
        pass
    
    
    def update(self):
        pass
    
    
    def delete(self):
        pass
    