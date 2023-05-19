from app.customUser.models import CustomUser
from .BasicManager import BasicManager

class UserManagerDB:    
    
    def __init__(self):
        self.manager = BasicManager(CustomUser)
        
    def get_by_id(self, user_id):
        return self.manager.get_by_id(object_id = user_id)