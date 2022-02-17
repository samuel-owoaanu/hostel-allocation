from django.urls import path
from .views import *

urlpatterns = [
   path('getroom', RoomView.as_view(), name="room"),
]
