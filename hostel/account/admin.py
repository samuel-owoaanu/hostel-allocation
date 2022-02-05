from django.contrib import admin
from .models import *

# admin - username
# mail@mail.com
# password - admin12345
# Register your adminModels here.

class AcademicStaffModel(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('department', 'phone_number',)

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(AcademicStaff, AcademicStaffModel)