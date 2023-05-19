from app.meet.models import Meet
from .BasicManager import BasicManager

class MeetManagerDB(BasicManager):
    
    
    def __init__(self):
        self.manager: BasicManager = BasicManager(Meet)
        
    def get_by_id(self, meet_id):
        return self.manager.get_by_id(object_id = meet_id)
    
    def create(self,date, start_time, end_time, status, professional, user, name_service):
        return self.manager.model.create(date=date, 
                    start_time=start_time,
                    end_time=end_time,
                    professional_name=professional,
                    status=status,
                    user_name=user, 
                    name_service=name_service)

                
    
    
    
    
    
    
    
    