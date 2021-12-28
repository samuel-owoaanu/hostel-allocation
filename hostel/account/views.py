from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, StudentsSerializer

# Create your views here.

class CreateUser(APIView):

    def get_users(self):
        try:
            return User.objects.all()
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        user = self.get_users()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)