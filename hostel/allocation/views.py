from os import stat
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hostel, Room, Student
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# Create your views here.
INVALID_REQUEST =Response({"Error":"Invalid Request"},status=400)

class RoomView(APIView):
    
    def get_room(self):
        try:
            return Room.objects.all()
        except Room.DoesNotExist:
            raise Http404
    
    def get(self, request, format=None):
        room = self.get_room()
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)