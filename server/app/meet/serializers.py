from rest_framework import serializers
from .models import Meet
from app.professionals.models import Professionals

class MeetSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Meet
        fields = ('id', 'date', 'start_time', 'end_time', 'cancelada', 'status',
                  'professional_name', 'user_name', 'name_service')
        # para campos de solo lectura agregamos
        read_only_fields = ('id','end_time','cancelada')
        
        
    def create(self, validated_data):
        print('ESTOY EN CREATE SERIALIZERS',validated_data)
        return ''
    
    def validate(self, attrs):
        print('ESTOY EN LAIDATA SERIALIZERS',attrs)
        return ''