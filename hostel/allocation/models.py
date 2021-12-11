from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Room(models.Model):
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.room_number

    class Meta:
        verbose_name_plural = 'Room'


class Hostel(models.Model):
    hostel_name = models.CharField(max_length=200, blank=False)
    hostel_type = models.CharField(max_length=200, blank=False)
    hostel_code = models.CharField(max_length=50, blank=False)
    hall_master = models.CharField(max_length=200, blank=False)
    chief_porter = models.CharField(max_length=200, blank=False)
    rooms = models.ManyToManyField(Room, blank=True)
    

    def __str__(self) -> str:
        return self.hostel_name

    class Meta:
        verbose_name_plural = 'Hostel'

