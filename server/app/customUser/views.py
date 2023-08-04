from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import logout
from .serializers import CustomUSerSerializer
from drf_yasg.utils import swagger_auto_schema



class Profile(APIView):
    authentication_classes = [SessionAuthentication]

    @swagger_auto_schema(
        tags=['Prueba'], operation_summary='Prueba 2'
    )
    def get(self, request, *args, **kwargs):
        # Si el usuario no está autenticado, redirigir a la página de inicio de sesión
        
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        # Obtener el usuario autenticado y serializarlo
        user = CustomUSerSerializer(request.user)
        
        # Devolver el usuario serializado
        return Response({"user": user.data}, status=status.HTTP_200_OK)

    
    @swagger_auto_schema(
        tags=['Prueba'], operation_summary='Prueba'
    )
    def post(self, request, *args, **kwargs):
        # Si el usuario no está autenticado, redirigir a la página de inicio de sesión
        return

class LogoutView(APIView):
    def post(self, request):
        # Cerrar la sesión actual del usuario
        logout(request)
        return Response(status=status.HTTP_200_OK)
