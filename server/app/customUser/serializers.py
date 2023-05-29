from rest_framework  import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model


class CustomUSerSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    tlf = serializers.CharField()
    address = serializers.CharField()   
        
        
    def create(self, validated_data, *args, **kwargs):
        instance = get_user_model()
        
        new_user = instance.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            tlf=validated_data['tlf'],
            address=validated_data['address'],
            
        )
        return new_user  
    
    def validate_username(self, value):
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError("El nombre de usuario ya existe")
        return value
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Convertir el campo UUID a una cadena para que sea serializable por JSON
        representation['id'] = str(representation['id'])
        return representation

class Admin_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
    
        