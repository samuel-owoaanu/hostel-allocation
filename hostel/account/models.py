from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models.enums import Choices
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        if not email:
            raise ValueError(_('Please, enter a valid email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff set to True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must be set to true'))
        
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email_address'), unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    other_name = models.CharField(max_length=100, blank=True, default=None, null=True)
    date_joined = models.DateTimeField(_('date_joined'), default=timezone.now)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = _('users')

class Student(models.Model):
    DEPARTMENT = (
        ('csc', 'Computer Science'),
        ('bch', 'BioChemistry'),
        ('mcb', 'MicroBiology'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    mat_no = models.CharField(max_length=30, blank=True, null=True, unique=True)
    department = models.CharField(choices=DEPARTMENT, blank=False, max_length=7)
    level = models.IntegerField(blank=False)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

class Non_AcademicStaff(models.Model):
    DEPARTMENT = (
        ('csc', 'Computer Science'),
        ('bch', 'BioChemistry'),
        ('mcb', 'MicroBiology'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(choices=DEPARTMENT, blank=False, max_length=7)

    def __str__(self) -> str:
        return self.user.email

class AcademicStaff(models.Model):
    DEPARTMENT = (
        ('csc', 'Computer Science'),
        ('bch', 'BioChemistry'),
        ('mcb', 'MicroBiology'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(choices=DEPARTMENT, blank=False, max_length=7)

    def __str__(self) -> str:
        return self.user.email
