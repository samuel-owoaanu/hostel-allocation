from os import stat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hostel
from .serializers import HostelSerializer
from rest_framework. response import Response
from rest_framework import serializers, status
from django.http import Http404

# Create your views here.
class HostelListView(APIView):

    def get_hostel(self):
        try:
            return Hostel.objects.all()
        except Hostel.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        rooms = self.get_hostel()
        serializer = HostelSerializer(rooms, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(): 
        pass

    def put():
        pass

    def delete():
        pass



class HostelList(APIView):

    def get(self, request, format=None):
        pass

    def post():
        pass

    def put():
        pass

    def delete():
        pass


def index(request):
    pass