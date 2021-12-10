from django.contrib import admin
from .models import *

# admin - username
# password - admin12345
# Register your models here.

admin.site.register(Room)
admin.site.register(Hostel)