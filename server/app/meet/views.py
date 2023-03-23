from datetime import datetime, time
from django_filters.rest_framework import DateRangeFilter, TimeRangeFilter
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Meet
from .serializers import MeetSerializer

# Create your views here.

class HorasDisponiblesView(generics.ListAPIView):
    serializer_class = MeetSerializer
    queryset = Meet.objects.filter(estado='disponible')
    filter_backends = [DateRangeFilter, TimeRangeFilter]

    def get_queryset(self):
        fecha = self.request.query_params.get('fecha', None)
        hora_inicial = datetime.strptime(fecha, '%Y-%m-%d').date() + time(hour=10)
        hora_final = datetime.strptime(fecha, '%Y-%m-%d').date() + time(hour=18)
        horas_disponibles = [hora_inicial]
        meets = self.filter_queryset(self.get_queryset())
        for meet in meets:
            if hora_inicial <= meet.hora < hora_final:
                horas_disponibles.remove(meet.hora)
        return horas_disponibles
    
    class ReservarCitaView(generics.CreateAPIView):
        serializer_class = MeetSerializer

    def create(self, request, *args, **kwargs):
        fecha = request.data.get('fecha')
        hora = request.data.get('hora')
        cliente = request.data.get('cliente')
        hora_reserva = datetime.strptime(fecha + ' ' + hora, '%Y-%m-%d %H:%M:%S')
        if hora_reserva.time() < time(hour=10) or hora_reserva.time() >= time(hour=18):
            return Response({'error': 'La hora seleccionada no está disponible'}, status=status.HTTP_400_BAD_REQUEST)
        if Meet.objects.filter(hora=hora_reserva, estado='reservada').exists():
            return Response({'error': 'La hora seleccionada ya está reservada'}, status=status.HTTP_400_BAD_REQUEST)
        meet = Meet.objects.create(hora=hora_reserva, cliente=cliente, estado='reservada')
        serializer = self.get_serializer(meet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CancelarCitaView(generics.DestroyAPIView):
    serializer_class = MeetSerializer
    queryset = Meet.objects.filter(estado='reservada')

    def destroy(self, request, *args, **kwargs):
        meet = self.get_object()
        meet.estado = 'disponible'
        meet.save()
        return Response({'message': 'La meet se ha cancelado correctamente'}, status=status.HTTP_204_NO_CONTENT)
