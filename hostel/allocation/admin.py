from django.contrib import admin
from .models import *

# admin - username
# password - admin12345
# Register your models here.
class RoomModel(admin.ModelAdmin):
    list_display = ('room_number', 'bed_spaces', 'max_occupancy', 'hostel_located',)
    
class RoomAllocationAdmin(admin.ModelAdmin):
    list_display = ('student', 'room', 'hostel', 'session',)

class HostelAdmin(admin.ModelAdmin):
    list_display = ('hostel_name', 'hostel_type', 'hostel_code',)
    search_fields = ('hostel_name', 'hostel_code',)

class SessionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Room, RoomModel)
admin.site.register(Hostel, HostelAdmin)
admin.site.register(Session)
admin.site.register(Room_Allocation, RoomAllocationAdmin)
