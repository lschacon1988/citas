from rest_framework import serializers
from .models import Meet

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meet
        fields = '__all__'