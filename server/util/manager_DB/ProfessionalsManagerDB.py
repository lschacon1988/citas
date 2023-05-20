from app.professionals.models import Professionals
from app.meet.models import Meet
from .BasicManager import BasicManager
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
class ProfessionalsManagerDB():   
    
    def __init__(self):
        self.manger: BasicManager = BasicManager(Professionals)
        
        
    def get_by_id(self, object_id):        
        return self.manger.get_by_id(object_id = object_id)
    
    
    def validate_availability(self, date, start_time, professional_name, ):
        
        return Meet.objects.filter(
                                Q(date=date) &
                                Q(start_time__lte=start_time) &
                                Q(end_time__gte=start_time) & 
                                Q(professional_name=professional_name)
                                ).prefetch_related('professional_name')
        
        