from rest_framework import viewsets, permissions
from .models import Service
from .serializer import ServiceSerializer
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ServiceSerializer
    
    @swagger_auto_schema(
        tags=["Services"],operation_summary="Get all services",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["Services"],operation_summary="Get service by id",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["Services"],operation_summary="create a service",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["Services"],operation_summary="update a service",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["Services"],operation_summary="partially update a service",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        tags=["Services"],operation_summary="delete a service",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)