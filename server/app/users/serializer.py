# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import UserProfile
# from .custon_create_form import CustomUserCreationForm


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password',
#                   'first_name', 'last_name',)
#         extra_kwargs = {'password': {'write_only': True}}


# class UserProfileSerializer(serializers.ModelSerializer):

#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = UserProfile
#         fields = ('id', 'tlf', 'username', 'password')

#     def create(self, validated_data):
#         print(validated_data)
#         username = validated_data.pop('username')
#         password = validated_data.pop('password')
#         user = CustomUserCreationForm(data=validated_data)
#         print('ESTOY AQUI', user)
#         if user.is_valid():
#             user = user.save(commit=False)
#             user.set_password(password)
#             user.username = username
#             user.save()
#             return user
#         raise serializers.ValidationError(user.errors)

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['username'] = instance.user.username
#         return representation

from rest_framework  import serializers
from .models import Client
from django.contrib.auth import get_user_model


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    tlf = serializers.CharField()
    address = serializers.CharField()
    
    # class Meta:
    #     model= CustomUser
    #     fields = ('id','email','username','password','first_name','last_name','tlf','address')
    #     read_only_fields =('id', )
        
        
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
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Convertir el campo UUID a una cadena para que sea serializable por JSON
        representation['id'] = str(representation['id'])
        return representation 
        