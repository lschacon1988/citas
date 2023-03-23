from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Service
        fields = ('id','name_service','duration')
        read_only_fields = ('id',)