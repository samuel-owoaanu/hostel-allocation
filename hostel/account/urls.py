from django.urls import path
from rest_framework import routers, urlpatterns
from .views import *

urlpatterns = [
    path("getusers", GetUser.as_view(), name="get_users"),
    path("getstudents", GetStudent.as_view(), name="get_students")
]