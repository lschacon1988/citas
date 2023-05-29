from rest_framework import serializers
from .models import Meet


class MeetSerializer(serializers.ModelSerializer):
    professionals_name = serializers.ReadOnlyField(source='professional.name')
    user_name = serializers.ReadOnlyField(source='user.first_name')

    class Meta:
        model = Meet
        fields = ('id', 'date', 'start_time', 'end_time', 'status',
                  'professional', 'professionals_name', 'user', 'user_name', 'name_service', 'status')
        # para campos de solo lectura agregamos
        read_only_fields = ('id', 'end_time', 'status',
                            'professionals_name', 'user_name')


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meet
        fields = '__all__'
