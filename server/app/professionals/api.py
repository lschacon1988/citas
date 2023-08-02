from rest_framework.response import Response
from rest_framework import viewsets, permissions
from app.professionals.models import Professionals
from app.customUser.models import CustomUser
from app.professionals.serializer import ProfessionalsSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
# Create your views here.


class ProfessionalsViewSet(viewsets.ModelViewSet):
    queryset = Professionals.objects.all()
    queryset_user = CustomUser.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProfessionalsSerializer

    @swagger_auto_schema(
        tags=["professionals"], operation_summary="Get a Professional",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["professionals"], operation_summary="Get a Professional",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["professionals"], operation_summary="Create a Professional",
    )
    def create(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(id=request.data["user"])
        except (KeyError, CustomUser.DoesNotExist) as error:
            return Response({"error": str(error),
                             "message":f'Usuario no encontrado en la base de datos'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfessionalsSerializer(data=request.data)

        if (serializer.is_valid()):
            user.is_staff = True
            serializer.save()
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=["professionals"], operation_summary="Update a Professional",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["professionals"], operation_summary="Partially Update a Professional",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["professionals"], operation_summary="Delete a Professional",
    )
    def destroy(self, request, *args, **kwargs):
        professionals = Professionals.objects.get(id=kwargs['pk'])
        user_relation_profecional = professionals.user
        user_relation_profecional.is_staff = False
        user_relation_profecional.save()
        
        return super().destroy(request, *args, **kwargs)
