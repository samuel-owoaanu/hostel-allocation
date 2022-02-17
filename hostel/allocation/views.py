from os import stat
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hostel, Room, Room_Allocation, Student
from .serializers import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
INVALID_REQUEST =Response({"Error":"Invalid Request"},status=400)

class HostelMGT(APIView):
    def get(self, request, pk=None, format = None):
        if pk is not None:
            hostelObj = Hostel.objects.get(pk=pk)
            serializer = HostelSerializer(hostelObj)
            hostel  = serializer.data
            available_rooms = list()
            allocated_rooms = list()
            unallocated_rooms = list()
            # filled_rooms =list()
            hostel['allocated_rooms'] = list()
            hostel['unallocated_rooms'] = list()
            # hostel['filled_rooms'] = list()
            hostel['available_rooms'] = int()
            hostel['rooms'] = list()
            

            room_obj = Room.objects.all()
            room_serializer = RoomSerializer(room_obj, many=True)
            rooms = room_serializer.data
            
            allocationOBJ = Room_Allocation.objects.all()
            allocations = serializeAllocation(allocationOBJ, many=True)
        
            for room in rooms:
                if room['Hostel_Located'] == hostel['id']:
                    hostel['rooms'].append(room['Room_Number'])
                    if not room['IsFull']:
                        available_rooms.append(room) 

            for allocation in allocations:
                if allocation['hostel'] == hostel['id'] :
                    for room in rooms:
                        if room['Hostel_Located'] == hostel['id']: 
                            """
                            For getting the list of rooms which are not empty
                            """
                            if allocation['room'] == room['id']:
                                allocated_rooms.append(room['Room_Number'])

            for room in rooms:
                if room['Hostel_Located'] == hostel['id'] and not room['Room_Number'] in allocated_rooms: 
                    """
                For getting the list of rooms which are not empty
                    """
                    # if allocation['room'] == room['id']:
                    unallocated_rooms.append(room['Room_Number']) 

                

            hostel['unallocated_rooms'] = unallocated_rooms
            hostel['allocated_rooms'] = allocated_rooms
            hostel['available_rooms']=len(available_rooms)
            return Response(hostel)

        else:
            # Gets list of all Hostels
            hostelObj = Hostel.objects.all()
            serializer = HostelSerializer(hostelObj, many=True)
            hostels  = serializer.data

            for hostel in hostels:    
                room_obj = Room.objects.all()
                room_serializer = RoomSerializer(room_obj, many=True)
                rooms = room_serializer.data
                hostel['rooms'] = list()

                for room in rooms:
                    if room['Hostel_Located'] == hostel['id'] and not room['IsFull']:
                        hostel['rooms'].append(room['Room_Number'])
                        pass
                pass    

            
            hostel_data = {
                'Hostel List':hostels
            }
            return Response(hostel_data, status=200)
        
    def post(self, request, pk=None):
        if pk is not None:
            hostelOBJ = Hostel.objects.get(pk=pk)
            serializer = HostelSerializer(hostelOBJ, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            # pass
        else:
            serializer = HostelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        return Response(serializer.errors, status=400)
    def delete(self, request, pk=None):

        if pk is not None:
            hostelOBJ = Hostel.objects.get(pk=pk)
            hostelOBJ.delete()
            return Response({"Deleted":True}, status = 200)
        else:
            return  INVALID_REQUEST

        pass
    
class RoomMGT(APIView):
    
    def get(self, request, hid=None, pk=None, format=None):
        """[summary]

        Args:
            request ([type]): [description]
            hid ([Int], optional): [Hostel ID]. Defaults to None.
            format ([type], optional): [description]. Defaults to None.

        Returns:
            [JSON Response]: [description]
        """
        if hid is not None and pk is None:
            roomObject = Room.objects.all()
            serializer = RoomSerializer(roomObject, many=True)
            rooms = serializer.data
            room_list = []
            hostel_name = ''
            hostel_code = ''
            
            for room in rooms:    
                hostel_obj = Hostel.objects.get(pk=hid)
                hostel_serializer = HostelSerializer(hostel_obj)
                hostel_location = hostel_serializer.data
                if hid == room['Hostel_Located']:
                    hostel_id = hostel_location['id']
                    hostel_name = hostel_location['Hostel_Name']+' ('+hostel_location['Hostel_Code']+')'
                    hostel_code = hostel_location['Hostel_Code']
                    room["Hostel_Located"] = hostel_location['Hostel_Code']
                    room_list.append(room)

            room_data = {
                'Hostel Id':hostel_id,
                'Hostel Name': hostel_name,
                'Hostel Code': hostel_code,
                'Rooms Data':{
                    "total_rooms":len(room_list),
                    "rooms":room_list
                }
            }

        elif pk is not None:
            roomObject = Room.objects.get(pk=pk)
            serializer = RoomSerializer(roomObject)
            room = serializer.data
            room_occupants = list()

            # check for allocated rooms
            allocationOBJ= Room_Allocation.objects.all()
            allocations = serializeAllocation(allocationOBJ, many=True)

            studentOBJ = Student.objects.all()
            students =serializeStudent(studentOBJ, many=True)

            for allocation in allocations:
                if room['id'] == allocation['room']:
                    for student in students:
                        if len(room_occupants) <= room['Bed_Spaces']:
                            if allocation['student'] == student['id']:
                                room_occupants.append(student['student_firstname']+" "+student['student_other_name']+" "+student['student_lastname'].upper()+" ("+str(student['level'])+" Level)")
                                
                        else:
                            break
                        pass
                    pass
            hostel_obj = Hostel.objects.get(pk=hid)
            hostel_serializer = HostelSerializer(hostel_obj)
            hostel_location = hostel_serializer.data
            if hid == room['Hostel_Located']:
                hostel_id = hostel_location['id']
                hostel_name = hostel_location['Hostel_Name']+' ('+hostel_location['Hostel_Code']+')'
                hostel_code = hostel_location['Hostel_Code']
                room["Hostel_Located"] = hostel_location['Hostel_Code']
                # room_list.append(room)

            room['occupants'] = room_occupants
            room_data ={
                "Room Data": room
                
            }


        else:
            return INVALID_REQUEST
        

        
        return Response(room_data)

    def post(self, request,hid=None, pk=None):
        if pk is not None:

            roomOBJ = Room.objects.get(pk=pk)
            serializer = RoomSerializer(roomOBJ, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            #  roomOBJ = Room.objects.get(pk=pk)
            serializer = RoomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request,hid=None, pk=None):

        if pk is not None:
            roomOBJ = Room.objects.get(pk=pk)
            roomOBJ.delete()
            return Response({"Deleted":True}, status = 200)
        else:
            return  INVALID_REQUEST

        
    

class AllocateRoom():
    pass


class AllocationList():
    pass

class AllocationDetail():
    pass



# Admin Views
class AdminLogin(APIView):
    pass

class StudentMGT(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            studentObj = Student.objects.get(pk=pk)
            serializer = StudentSerializer(studentObj)
            student = serializer.data

            allocationOBJ = Room_Allocation.objects.all()
                
            allocation = serializeAllocation(allocationOBJ, many=True)
                
                # print(student_['id'])
            for allocation_ in allocation:

                if allocation_['student'] == student['id'] and allocation_['room'] is not None:
                    roomOBJ = Room.objects.get(pk=allocation_['room'])
                    room = serializeRoom(roomOBJ)
                    hostelOBJ = Hostel.objects.get(pk=room['Hostel_Located'])
                    hostel = serializeHostel(hostelOBJ)
                    student['is_allocated'] = True 
                    student['room-allocated'] = room['Room_Number']+' ('+hostel['Hostel_Name']+' - '+hostel['Hostel_Code']+')'
                elif not student.__contains__('room-allocated'): 
                    student['is_allocated'] = False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                    student['room-allocated'] = "Not yet Allocated"
                        # pass
            # print(request.headers)
            return Response(student)
        else:
            studentObj = Student.objects.all()
            serializer = StudentSerializer(studentObj, many=True)
            students = serializer.data
            
            for student_ in students:
                student_pk = int(student_['id'])
                student_.pop('email')
                student_.pop('department')
                # student_pk = 
                allocationOBJ = Room_Allocation.objects.all()
                
                allocation = serializeAllocation(allocationOBJ, many=True)
                
                # print(student_['id'])
                for allocation_ in allocation:

                    if allocation_['student'] == student_pk and allocation_['room'] is not None:
                        roomOBJ = Room.objects.get(pk=allocation_['room'])
                        room = serializeRoom(roomOBJ)
                        hostelOBJ = Hostel.objects.get(pk=room['Hostel_Located'])
                        hostel = serializeHostel(hostelOBJ)
                        student_['is_allocated'] = True
                        student_['room-allocated'] = room['Room_Number']+' ('+hostel['Hostel_Name']+' - '+hostel['Hostel_Code']+')'
                    elif not student_.__contains__('room-allocated'):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                        student_['is_allocated'] = False
                        student_['room-allocated'] = "NONE"
                        # pass
                
            return Response(students)
        

    def post(self, request, pk=None):
        
        if pk is not None:
            studentOBJ = Student.objects.get(pk=pk)
            serializer = StudentSerializer(studentOBJ, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            # pass
        else:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        
        studentOBJ = Student.objects.get(pk=pk)
        studentOBJ.delete()
        return Response({"Deleted":True}, status = 200)


class SessionMGT(APIView):
    pass

class AllocationMGT(APIView):
    def get(self, request, format=None):
        pass
    def post(self, request):
        pass