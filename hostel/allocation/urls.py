from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1', HostelListView.as_view(), name='hostels'),
    # path('', index)
]
