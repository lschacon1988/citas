from rest_framework import serializers
from .models import Meet
from app.professionals.models import Professionals

class MeetSerializer(serializers.ModelSerializer):
    professionals_name = serializers.CharField(write_only=True)
    class Meta:
        model= Meet
        fields = ('id','date','hour','professional_id','professionals_name','user_id','service_id', 'activa')
        # para campos de solo lectura agregamos
        read_only_fields =('id', 'professionals_name')
        
        def create(self, validated_data):
            professionals_name = validated_data.pop('professionals_name')
            professionals = Professionals.objects.get(name=professionals_name)
            book = Meet.objects.create(professionals=professionals, **validated_data)
            return book
        
        def update(self, instance, validated_data):
            professionals_name = validated_data.pop('professionals_name', None)
            if professionals_name:
                professionals = Professionals.objects.get(name=professionals_name)
                instance.professionals_id = professionals
            instance.hour = validated_data.get('hour', instance.hour)
            instance.save()
            return instance
        
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['professionals_name'] = instance.professional_id.name if instance.professional_id else None
        return ret
        
        
        
        
        
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