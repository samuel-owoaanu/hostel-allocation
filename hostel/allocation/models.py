from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Hostel(models.Model):
    HostelName = models.CharField(max_length=200, blank=False)
    HostelType = models.CharField(max_length=200, blank=False)
    HostelCode = models.CharField(max_length=50, blank=False)
    HallMaster = models.CharField(max_length=200, blank=False)
    ChiefPorter = models.CharField(max_length=200, blank=False)
    

    def __str__(self) -> str:
        return self.HostelName

    class Meta:
        verbose_name_plural = 'Hostel'



class Room(models.Model):
    RoomNumber = models.CharField(max_length=20, blank=False)
    BedSpaces = models.IntegerField()
    IsFull = models.BooleanField(default=False)
    HostelLocated = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self):
        return self.RoomNumber

    class Meta:
        verbose_name_plural = 'Room'



