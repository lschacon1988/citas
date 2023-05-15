from rest_framework import viewsets, permissions
from .models import Client
from .serializer import  UserSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer