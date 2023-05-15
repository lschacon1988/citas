from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import logout
from .serializers import CustomUSerSerializer


class Profile(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request, *args, **kwargs):
        # Si el usuario no está autenticado, redirigir a la página de inicio de sesión
        
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        # Obtener el usuario autenticado y serializarlo
        user = CustomUSerSerializer(request.user)
        
        # Devolver el usuario serializado
        return Response({"user": user.data}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        # Cerrar la sesión actual del usuario
        logout(request)
        return Response(status=status.HTTP_200_OK)
