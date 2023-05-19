from rest_framework.response import Response
from rest_framework import viewsets, permissions
from django.core.exceptions import ObjectDoesNotExist

from .models import Meet
from .serializers import MeetSerializer

from util.manager_DB.ServicesManagerDB import ServicesManagerDB
from util.manager_DB.ProfessionalsManagerDB import ProfessionalsManagerDB
from util.manager_DB.UserManagerDB import UserManagerDB
from util.manager_DB.MeetMangerDB import MeetManagerDB
from util.calculate_end_of_turn import calculate_end_of_turn

# Create your views here.

format_hours = "%H:%M"


class MeetViewSet(viewsets.ModelViewSet):
    queryset = Meet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MeetSerializer

    def create(self, request, *args, **kwargs):
        (_, date, start_time,  status, professional_name,
         user_name, name_service) = request.data.values()

        servisManager = ServicesManagerDB()
        professionalManager = ProfessionalsManagerDB()
        meetManager = MeetManagerDB()
        userManager = UserManagerDB()

        try:
            try:
                service = servisManager.get_by_name(name_service=name_service)

                professional = professionalManager.get_by_id(
                    object_id=professional_name)

                user = userManager.get_by_id(user_id=user_name)

            except ObjectDoesNotExist as error:
                return Response(f'{error}')

            end_time = calculate_end_of_turn(self, start_time=start_time,
                                            duration_turn=service.duration,
                                            format_hours=format_hours)

            professional_not_available = professionalManager.validate_availability(
                professional_name=professional_name,
                start_time=start_time,
                date=date)

            if not professional_not_available.exists():

                new_meet = meetManager.create(date=date,
                                            end_time=end_time,
                                            start_time=start_time,
                                            status=status,
                                            professional=professional,
                                            user=user,
                                            name_service=service.name_service)

                return Response(MeetSerializer(new_meet).data)

            return Response("Nuestra profecional no esta disponible en este horario.")
        except KeyError:

            return Response(f'algo salio mal {KeyError}', status=400)
