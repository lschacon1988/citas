from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import logout
from .serializers import CustomUSerSerializer, Superuser_serializer
from drf_yasg.utils import swagger_auto_schema

from .models import CustomUser


class Profile(APIView):
    queryset = CustomUser.objects.all()
    authentication_classes = [SessionAuthentication]

    @swagger_auto_schema(
        tags=['Admin'], operation_summary='retorna el perfil del usuario logeado'
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
        tags=['Admin'],
        operation_summary='Crea un unico super usuario',
        request_body=Superuser_serializer,
    )
    def post(self, request, *args, **kwargs):
        superuser_exists = self.queryset.filter(is_superuser=True)
        if len(superuser_exists) > 0:
            return Response({'Message': 'Superuser already exists'}, status=status.HTTP_409_CONFLICT)
        
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        
        if(not username or not password or not email):
            return Response({'Message': 'Missing data'}, status=status.HTTP_400_BAD_REQUEST)
        
        new_superuse = Superuser_serializer(data=request.data)

        if new_superuse.is_valid():
            new_superuse.save()
            return Response(new_superuse.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        # Cerrar la sesión actual del usuario
        logout(request)
        return Response(status=status.HTTP_200_OK)
