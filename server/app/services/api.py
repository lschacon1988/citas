from rest_framework import viewsets, permissions
from .models import Service
from .serializer import ServiceSerializer
# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ServiceSerializer