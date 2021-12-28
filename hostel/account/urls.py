from django.urls import path
from rest_framework import routers, urlpatterns
from .views import *

urlpatterns = [
    path("create", CreateUser.as_view(), name="create_user")
]