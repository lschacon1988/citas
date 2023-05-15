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
        




   

        
        
        
        
        
    #     professionals_name = serializers.CharField(write_only=True)

    # class Meta:
    #     model = Book
    #     fields = ('id', 'title', 'author', 'author_name')

    # def create(self, validated_data):
    #     author_name = validated_data.pop('author_name')
    #     author = Author.objects.get(name=author_name)
    #     book = Book.objects.create(author=author, **validated_data)
    #     return book

    # def update(self, instance, validated_data):
    #     author_name = validated_data.pop('author_name', None)
    #     if author_name:
    #         author = Author.objects.get(name=author_name)
    #         instance.author = author
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.save()
    #     return instance

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['author_name'] = instance.author.name if instance.author else None
    #     return ret