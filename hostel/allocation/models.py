from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields.related import ForeignKey
from account.models import Student
# from django.db.models.fields.reverse_related import ManyToManyRel

# Create your models here.

class Hostel_Type(models.Model):
    
    hostel_type_name = models.CharField(max_length=100, blank=False)
    type_amount = models.FloatField()
    
    pass    


class Hostel(models.Model):
    Hostel_Name = models.CharField(max_length=200, blank=False)
    Hostel_Type = models.CharField(max_length=200, blank=False)
    Hostel_Code = models.CharField(max_length=50, blank=False)
    Hall_Master = models.CharField(max_length=200, blank=False)
    Chief_Porter = models.CharField(max_length=200, blank=False)
    

    def __str__(self) -> str:
        return self.Hostel_Name+" ("+self.Hostel_Code+")"

    class Meta:
        verbose_name_plural = "Hostel"

class Room(models.Model):
    Room_Number = models.CharField(max_length=20, blank=False)
    Bed_Spaces = models.IntegerField()
    IsFull = models.BooleanField(default=False)
    Hostel_Located = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.Room_Number)+" - "+str(self.Hostel_Located)

    class Meta:
        verbose_name_plural = "Room"


class Session(models.Model):
    session_name = models.CharField(max_length=100, blank=False)
    session_start = models.DateField(blank=False)
    session_end = models.DateField(blank=False)

    def __str__(self) -> str:
        return self.session_name

    class Meta:
        verbose_name_plural = 'Session'


# class Payment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     reference_number = models.CharField(max_length=150)
#     amount = models.FloatField()
#     payment_status = models.BooleanField(default=False)
#     if payment_status is False:
#         status_info = 'UNPAID'
#     else:
#         status_info = 'PAID'

#     def __str__(self) -> str:
#         return self.student + ' ('+self.status_info+')'


class Room_Allocation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, blank=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=False)
    # name = models.CharField(max_length=50, blank=False)
    def __str__(self):
        # return self.name

        return str(self.student) + ' ('+str(self.room)+')'## in '+str(self.hostel)+')'

    class Meta:
        verbose_name_plural = 'Allocation'