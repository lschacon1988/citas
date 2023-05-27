from rest_framework import serializers
from .models import Meet
from app.professionals.models import Professionals

class MeetSerializer(serializers.ModelSerializer):
    professionals_name = serializers.ReadOnlyField(source='professional.name')
    user_name = serializers.ReadOnlyField(source='user.first_name')

    class Meta:
        model = Meet
        fields = ('id', 'date', 'start_time', 'end_time', 'cancelada', 'status',
                  'professional','professionals_name', 'user', 'user_name', 'name_service','status')
        # para campos de solo lectura agregamos
        read_only_fields = ('id','end_time','cancelada','status', 'professionals_name','user_name')
        
        extra_kwargs = {
            'status': {'read_only': False},
            'cancelada':{ 'read_only': False},
            
            
            # Agrega otros campos que deseas permitir que el administrador modifique aquí
        }