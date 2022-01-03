# from ..models import *

class HostelLIB():
    def __init__(self, id, name, type, code, master, c_porter, rooms) -> None:
                
        self.id=id
        self.hostel_name =name
        self.hostel_type = type
        self.hostel_code = code
        self.hall_master =master
        self.chief_porter =c_porter
        self.rooms = rooms

    # def 

class RoomLIB(): 
    def __init__(self, id, name,type, spaces, hostel, session, occupants) -> None:
        
        self.id =''
        self.room_name = ''
        self.bed_spaces = ''
        self.hostel_located = ''
        self.session = ''
        # Member object format
        """member ={
            name:...membername
            level:...memberlevel
        }
        """
        self.room_members = []
        self.isFull = False  

    
    def check_room_availability(hostel_id):
        """[to check for the rooms vailable for allocation]

        Args:
            hostel_id (int): the id of thr hostel under 
        """
        pass

    def check_room_members(hostel_id, room_id):
        pass

    def allocate_room(hostel_id, room_id, student_id):
        pass
    
    def update_allocation():
        pass


    pass

class StudentDataLIB():
    pass

class SystemAdminsLIB():
    pass

