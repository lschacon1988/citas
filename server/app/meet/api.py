from drf_yasg.utils import swagger_auto_schema
from django.conf import settings
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from .models import Meet
from .serializers import MeetSerializer, AdminSerializer


from util.manager_DB.ServicesManagerDB import ServicesManagerDB
from util.manager_DB.ProfessionalsManagerDB import ProfessionalsManagerDB
from util.manager_DB.UserManagerDB import UserManagerDB
from util.manager_DB.MeetMangerDB import MeetManagerDB
from util.calculate_end_of_turn import calculate_end_of_turn


# Create your views here.

format_hours = "%H:%M:%S"


class MeetViewSet(viewsets.ModelViewSet):
    queryset = Meet.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action in ['update', 'partial_update']:
            return [permissions.IsAdminUser()]
        else:
            return [permissions.AllowAny()]

    def get_serializer(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return MeetSerializer(*args, **kwargs)
        else:
            return MeetSerializer(*args, **kwargs)

    @swagger_auto_schema(
        tags=['Meet'], operation_summary='Lista todos los meet'

    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Meet'], operation_summary='lee los meet'
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Meet'], operation_summary='Crea un meet'

    )
    def create(self, request, *args, **kwargs):
        print('/*/*//', request.data)
        # (_, date, start_time,  professional,
        #  user, name_service) = request.data.values()
        data = request.data

        servisManager = ServicesManagerDB()
        professionalManager = ProfessionalsManagerDB()
        meetManager = MeetManagerDB()
        userManager = UserManagerDB()

        try:
            try:
                service = servisManager.get_by_name(
                    name_service=data['name_service'])

                professional = professionalManager.get_by_id(
                    object_id=data['professional'])

                user = userManager. get_by_id(user_id=data['user'])

            except ObjectDoesNotExist as error:
                return Response(f'{error}', status=400)

            end_time = calculate_end_of_turn(self, start_time=data['start_time'],
                                             duration_turn=service.duration,
                                             format_hours=format_hours)

            professional_not_available = professionalManager.validate_availability(
                professional=professional,
                start_time=data['start_time'],
                date=data['date'])

            if not professional_not_available.exists():

                new_meet = meetManager.create(date=data['date'],
                                              end_time=end_time,
                                              start_time=data['start_time'],
                                              professional=professional,
                                              user=user,
                                              name_service=service.name_service)

                contex = {
                    'fecha': data['date'],
                    'hora_inicio': data['start_time'],
                    'hora_fin': end_time,
                    'profecional_name': professional.user.first_name,
                    'user_name': user.first_name,
                    'service_name': service.name_service,
                }

                asunto = 'Confirmación de cita'
                mensaje_html = render_to_string(
                    'confirmacion.html', context=contex)
                mensaje_texto = strip_tags(mensaje_html)
                destinatario = [user.email]

                send_mail(asunto, mensaje_texto, settings.DEFAULT_FROM_EMAIL,
                          destinatario, html_message=mensaje_html)

                return Response(MeetSerializer(new_meet).data, status=201)

            return Response("Nuestra profecional no esta disponible en este horario.", status=400)
        except KeyError as error:

            return Response(f'algo salio mal {error}', status=500)

    @swagger_auto_schema(
        tags=['Meet'], operation_summary='Actualiza un meet'
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Meet'], operation_summary='Actualiza un meet'
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Meet'], operation_summary='Elimina un meet'
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
