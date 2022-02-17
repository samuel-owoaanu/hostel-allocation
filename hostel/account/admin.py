from django.contrib import admin
from .models import *

# admin - username
# mail@mail.com
# password - admin12345
# Register your adminModels here.

class AcademicStaffModel(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('department', 'phone_number',)

class UserModel(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'other_name',)
    search_fields = ('email', 'first_name', 'last_name',)

class StudentModel(admin.ModelAdmin):
    list_display = ('mat_no', 'department', 'level',)
    search_fields = ('mat_no', 'department', 'level',)

# Register your models here.
admin.site.register(User, UserModel)
admin.site.register(Student, StudentModel)
admin.site.register(AcademicStaff, AcademicStaffModel)