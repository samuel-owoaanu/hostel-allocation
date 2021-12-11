from django.db.models import fields
from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_number',)

class HostelSerializer(serializers.ModelSerializer):
    rooms = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Hostel
        fields = ('id', 'hostel_name', 'hostel_type', 'hostel_code', 'hall_master', 'chief_porter', 'rooms')
