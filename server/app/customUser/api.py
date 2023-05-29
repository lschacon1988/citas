from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUSerSerializer, Admin_user_serializer

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomUSerSerializer
    
   
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return Admin_user_serializer
        else:
            return CustomUSerSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = CustomUSerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        