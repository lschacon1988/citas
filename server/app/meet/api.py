from rest_framework import viewsets, permissions
from .models import Meet
from .serializers import MeetSerializer 
# Create your views here.
class MeetViewSet(viewsets.ModelViewSet):
    queryset = Meet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MeetSerializer
    
    