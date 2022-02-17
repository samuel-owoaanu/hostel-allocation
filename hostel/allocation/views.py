from os import stat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hostel, Room, Student
from .serializers import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
INVALID_REQUEST =Response({"Error":"Invalid Request"},status=400)

