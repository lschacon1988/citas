# from datetime import datetime, time
# from django_filters.rest_framework import DateRangeFilter, TimeRangeFilter
# from rest_framework import generics, status
# from rest_framework.response import Response
# from .models import Cita
# from .serializers import CitaSerializer

# class HorasDisponiblesView(generics.ListAPIView):
#     serializer_class = CitaSerializer
#     queryset = Cita.objects.filter(estado='disponible')
#     filter_backends = [DateRangeFilter, TimeRangeFilter]

#     def get_queryset(self):
#         fecha = self.request.query_params.get('fecha', None)
#         hora_inicial = datetime.strptime(fecha, '%Y-%m-%d').date() + time(hour=10)
#         hora_final = datetime.strptime(fecha, '%Y-%m-%d').date() + time(hour=18)
#         horas_disponibles = [hora_inicial]
#         citas = self.filter_queryset(self.get_queryset())
#         for cita in citas:
#             if hora_inicial <= cita.hora < hora_final:
#                 horas_disponibles.remove(cita.hora)
#         return horas_disponibles

# class ReservarCitaView(generics.CreateAPIView):
#     serializer_class = CitaSerializer

#     def create(self, request, *args, **kwargs):
#         fecha = request.data.get('fecha')
#         hora = request.data.get('hora')
#         cliente = request.data.get('cliente')
#         hora_reserva = datetime.strptime(fecha + ' ' + hora, '%Y-%m-%d %H:%M:%S')
#         if hora_reserva.time() < time(hour=10) or hora_reserva.time() >= time(hour=18):
#             return Response({'error': 'La hora seleccionada no está disponible'}, status=status.HTTP_400_BAD_REQUEST)
#         if Cita.objects.filter(hora=hora_reserva, estado='reservada').exists():
#             return Response({'error': 'La hora seleccionada ya está reservada'}, status=status.HTTP_400_BAD_REQUEST)
#         cita = Cita.objects.create(hora=hora_reserva, cliente=cliente, estado='reservada')
#         serializer = self.get_serializer(cita)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class CancelarCitaView(generics.DestroyAPIView):
#     serializer_class = CitaSerializer
#     queryset = Cita.objects.filter(estado='reservada')

#     def destroy(self, request, *args, **kwargs):
#         cita = self.get_object()
#         cita.estado = 'disponible'
#         cita.save()
#         return Response({'message': 'La cita se ha cancelado correctamente'}, status=status.HTTP_204_NO_CONTENT)


# from django.urls import path
# from .views import HorasDisponiblesView, ReservarCitaView, CancelarCitaView

# urlpatterns = [
#     path('horas-disponibles/', HorasDisponiblesView.as_view(), name='horas_disponibles'),
#     path('reservar-cita/', ReservarCitaView.as_view(), name='reservar_cita'),
#     path('cancelar-cita/<int:pk>/', CancelarCitaView.as_view(), name='cancelar_cita'),
# ]




# from django.db import models
# from django.contrib.auth.models import User

# class Service(models.Model):
#     name = models.CharField(max_length=255)
#     duration = models.PositiveIntegerField() # Duración en minutos
    
# class Professional(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     services = models.ManyToManyField(Service)
    
# class Meet(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
    
#     def save(self, *args, **kwargs):
#         if self.start_time.time() < datetime.time(9, 0) or self.end_time.time() > datetime.time(18, 0):
#             raise ValidationError("Las citas solo pueden ser programadas entre las 9 AM y las 6 PM.")
#         duration = (self.end_time - self.start_time).total_seconds() / 60
#         if duration != self.service.duration:
#             raise ValidationError("La duración de la cita debe ser igual a la duración del servicio.")
#         super(Meet, self).save(*args, **kwargs)