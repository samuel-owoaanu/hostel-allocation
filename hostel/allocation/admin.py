from django.contrib import admin
from .models import *

# admin - username
# password - admin12345
# Register your models here.
class RoomModel(admin.ModelAdmin):
    list_display = ('Room_Number', 'Bed_Spaces',)
    
class RoomAllocationAdmin(admin.ModelAdmin):
    list_display = ('student', 'room', 'hostel', 'session',)

admin.site.register(Room, RoomModel)
admin.site.register(Hostel)
admin.site.register(Session)
admin.site.register(Room_Allocation, RoomAllocationAdmin)
