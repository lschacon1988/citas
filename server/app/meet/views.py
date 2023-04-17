from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import MeetSerializer
from .models import Meet


class MeetView(viewsets.ViewSet):

    def post(self, request, *args, **kwargs):
        prueba = self.request.body
        print(prueba)
        return Response('')
