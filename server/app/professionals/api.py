from rest_framework import viewsets, permissions
from app.professionals.models  import Professionals
from app.professionals.serializer import ProfessionalsSerializer
# Create your views here.
class ProfessionalsViewSet(viewsets.ModelViewSet):
    queryset = Professionals.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfessionalsSerializer