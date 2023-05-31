from rest_framework import serializers
from app.professionals.models import Professionals 

class ProfessionalsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Professionals
        fields = '__all__'
        
        