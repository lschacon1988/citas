from rest_framework  import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields = ('id','name','lastname','email','tlf','password')
        
        read_only_fields = ('id','password')