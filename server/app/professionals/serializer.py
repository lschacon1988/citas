from rest_framework import serializers
from app.professionals.models import Professionals 

class ProfessionalsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Professionals
        fields = ('id','name','lastname','specialty','tlf','admission_date')
        
        read_only_fields = ('admission_date','id')