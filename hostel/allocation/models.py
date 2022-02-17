import uuid
from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields.related import ForeignKey
from django.core.exceptions import ValidationError
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
        return self.hostel_name + " " + "Hostel"

    class Meta:
        verbose_name_plural = "Hostel"

class Session(models.Model):
    session_name = models.CharField(max_length=100, blank=False)
    session_start = models.DateField(blank=False)
    session_end = models.DateField(blank=False)

    def __str__(self) -> str:
        return self.session_name

    class Meta:
        verbose_name_plural = 'Session'

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_number = models.CharField(max_length=20, blank=False)
    bed_spaces = models.IntegerField()
    max_occupancy = models.IntegerField()
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)

    def __str__(self) -> str:
        return str(self.room_number)

    def save(self, *args, **kwargs):
        room_count = Room.objects.all()
        print(room_count)
        if len(self.student.all()) >= self.max_occupancy:
            raise ValidationError('Room is full')

        # if Student.objects.filter(level=self.student.level).count() > 1:
        # print(self.student.all())
        # if len(self.student.all()) > 1:
            
        #     raise ValidationError('This level already exists.')

        super(Room, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Room"
