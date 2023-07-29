from rest_framework import viewsets, permissions
from app.professionals.models  import Professionals
from app.professionals.serializer import ProfessionalsSerializer
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
class ProfessionalsViewSet(viewsets.ModelViewSet):
    queryset = Professionals.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProfessionalsSerializer
    
    
    @swagger_auto_schema(
        tags=["professionals"],operation_summary="Get a Professional",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["professionals"],operation_summary="Get a Professional",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)        
    
    @swagger_auto_schema(
        tags=["professionals"],operation_summary="Create a Professional",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["professionals"],operation_summary="Update a Professional",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["professionals"],operation_summary="Partially Update a Professional",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["professionals"],operation_summary="Delete a Professional",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)