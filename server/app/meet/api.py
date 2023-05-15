import datetime
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


from .serializers import MeetSerializer
from ..professionals.serializer import ProfessionalsSerializer
from ..services.serializer import ServiceSerializer
from ..users.serializer import UserSerializer

from ..professionals.models import Professionals
from ..services.models import Service
from ..users.models import Client
from .models import Meet
# Create your views here.


format_hours = "%H:%M"


class MeetViewSet(viewsets.ModelViewSet):
    queryset = Meet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MeetSerializer

    def create(self, request, *args, **kwargs):
        (_, date, start_time,  status, professional_name,
         user_name, name_service) = request.data.values()
        try:
            
            try:
                service = Service.objects.get(name_service=name_service)
            except ObjectDoesNotExist:
                return Response('El servicio ' + name_service + 'no esta disponible')
            try:

                professional = Professionals.objects.get(id=professional_name)

            except ObjectDoesNotExist:
                return Response(f'La profecional {professional_name} no esta disponible')
            try:

                user = Client.objects.get(id=user_name)
            except ObjectDoesNotExist:
                return Response(f'user no encontardo')

            end_time = str(datetime.datetime.strptime(
                start_time, format_hours) + service.duration - datetime.datetime(1900, 1, 1))
            
            space_not_available = Meet.objects.filter(Q(date=date) & Q(start_time__lte=start_time) &
                                          Q(end_time__gte=start_time) & Q(professional_name=professional_name)).prefetch_related('professional_name')
            

            if not space_not_available.exists():
                new_meet = Meet(date=date, start_time=start_time, end_time=end_time,
                                professional_name=professional, status=status, user_name=user, name_service=name_service)
                new_meet.save()
                return Response(MeetSerializer(new_meet).data)

            return Response("Nuestra profecional no esta disponible en este horario.")
        except KeyError:
            print('algo salio mal')
            return Response(f'algo salio mal {KeyError}', status= 400)
