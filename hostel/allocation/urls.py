from django.urls import path
from .views import *

urlpatterns = [
    path('', HostelList.as_view(), name='hostels'),
    # path('', index)
]
