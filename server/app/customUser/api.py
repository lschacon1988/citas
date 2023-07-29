from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUSerSerializer, Admin_user_serializer
from drf_yasg.utils import swagger_auto_schema

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
    
    @swagger_auto_schema(
        tags=["User"],operation_summary="List all users"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["User"],operation_summary="Retrieve a user"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(
        tags=["User"],operation_summary="Create a new user")
    def create(self, request, *args, **kwargs):
        serializer = CustomUSerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
        tags=["User"],operation_summary="Update a user"
    ) 
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["User"],operation_summary="Partially update a user"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["User"],operation_summary="Delete a user"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)