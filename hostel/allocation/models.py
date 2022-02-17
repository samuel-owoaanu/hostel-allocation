from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields.related import ForeignKey
from django.forms import ValidationError
from account.models import Student
# from django.db.models.fields.reverse_related import ManyToManyRel

# Create your models here.

class Hostel_Type(models.Model):
    
    hostel_type_name = models.CharField(max_length=100, blank=False)
    type_amount = models.FloatField()
    
    pass    


class Hostel(models.Model):
    hostel_name = models.CharField(max_length=200, blank=False)
    hostel_type = models.CharField(max_length=200, blank=False)
    hostel_code = models.CharField(max_length=50, blank=False)
    hall_master = models.CharField(max_length=200, blank=False)
    chief_porter = models.CharField(max_length=200, blank=False)
    

    def __str__(self) -> str:
        return self.Hostel_Name+" ("+self.Hostel_Code+")"

    class Meta:
        verbose_name_plural = "Hostel"

class Room(models.Model):
    room_number = models.CharField(max_length=20, blank=False)
    bed_spaces = models.IntegerField()

    isFull = models.BooleanField(default=False)
    hostel_located = models.ForeignKey(Hostel, on_delete=models.CASCADE)

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

class Room_Allocation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, blank=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=False)
    # name = models.CharField(max_length=50, blank=False)
    def __str__(self):
        # return self.name

        return str(self.student) + ' ('+str(self.room)+')'## in '+str(self.hostel)+')'

    def save(self, *args, **kwargs):
        # user = self.student
        room = self.room

        if room.Bed_Spaces < self.student.id:
            raise ValidationError("Room is full".format(room.Bed_Spaces))

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Allocation'