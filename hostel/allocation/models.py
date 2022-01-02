from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Room(models.Model):
    room_number = models.CharField(max_length=5, blank=False)
    bed_spaces = models.CharField(max_length=5, blank=False)
    hostel_located = models.CharField(max_length=20, blank=False)
    is_full = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.room_number

    class Meta:
        verbose_name_plural = "Room"

class Session(models.Model):
    SESSION = (
        ('first', 'First Semester'),
        ('second', 'Second Semester'),
    )
    session_name = models.CharField(choices=SESSION, blank=False, max_length=10)
    session_start = models.DateField()
    session_end = models.DateField()

    def __str__(self) -> str:
        return self.session_name

    class Meta:
        verbose_name_plural = "Session"

class HostelType(models.Model):
    hostel_type_name = models.CharField(max_length=50, blank=False)
    hostel_type_amount = models.DecimalField(max_digits=10, blank=False, decimal_places=2)

    def __str__(self) -> str:
        return self.hostel_type_name

    class Meta:
        verbose_name_plural = "HostelType"

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=50, blank=False)
    hall_master = models.CharField(max_length=30, blank=False)
    chief_porter = models.CharField(max_length=30, blank=False)
    hostel_code = models.CharField(max_length=20, blank=False)
    hostel_type = models.ForeignKey(HostelType, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.hostel_name

    class Meta:
        verbose_name_plural = "Hostel"

