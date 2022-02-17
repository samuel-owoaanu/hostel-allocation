from django.db.models import fields
from rest_framework import serializers
from .models import Hostel, Room, Student

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    hostel = serializers.StringRelatedField()
    session = serializers.StringRelatedField()
    student = serializers.StringRelatedField(many=True)
    class Meta:
        model = Room
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


# class AllocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room_Allocation
#         fields = "__all__"

# def serializeAllocation(allocation_instace, many=False):
#     if many is not False:
#         serializer = AllocationSerializer(allocation_instace, many=True)
#     else:
#         serializer = AllocationSerializer(allocation_instace)

#     allocation = serializer.data
#     return allocation

# def serializeRoom(room_instance, many=False):
#     if many is not False:
#         serializer = RoomSerializer(room_instance, many=True)
#     else:
#         serializer = RoomSerializer(room_instance)

#     room = serializer.data
#     return room

# def serializeHostel(hostel_instance, many=False):
#     if many is not False:
#         serializer = HostelSerializer(hostel_instance, many=True)
#     else:
#         serializer = HostelSerializer(hostel_instance)

#     hostel = serializer.data
#     return hostel

# def serializeStudent(stud_instance, many=False):
#     if many is not False:
#         serializer = StudentSerializer(stud_instance, many=True)
#     else:
#         serializer = StudentSerializer(stud_instance)

#     student = serializer.data
#     return student
