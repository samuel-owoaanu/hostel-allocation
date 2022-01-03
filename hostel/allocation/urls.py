from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/v1/hostel-list', HostelMGT.as_view(), name='Hostel List'),
    path('api/v1/hostel-detail/<int:pk>', HostelMGT.as_view(), name='Hostel Detail'),
    path('api/v1/delete-hostel/<int:pk>', HostelMGT.as_view(), name='Delete Hostel'),
    path('api/v1/hostel/<int:hid>/room-list/', RoomMGT.as_view(), name='Room List'),
    # hid -> Hostel ID
    
    path('api/v1/hostel/<int:hid>/room-detail/<int:pk>', RoomMGT.as_view()),
    # Admin endpoints
    path('api/v1/admin/login/', AdminLogin.as_view(),),
    
    # Student MGT Endpoints
    path('api/v1/admin/student-list/', StudentMGT.as_view(),),
    path('api/v1/admin/student-detail/<int:pk>', StudentMGT.as_view(),),
    # path('api/v1/admin/create-student', AdminLogin.as_view(),),
    # path('api/v1/admin/update-student/', AdminLogin.as_view(),),
    # path('api/v1/admin/delete-student/', AdminLogin.as_view(),),
    # path('api/v1/admin/student-mgt/', StudentMGT.as_view(),),

    # School Session MGT 
    path('api/v1/admin/session-list', SessionMGT.as_view(),),
    path('api/v1/admin/session-mgt', SessionMGT.as_view(),),

    # Hostel MGT
    path('api/v1/admin/hostel-mgt/', HostelMGT.as_view(),),

    # Allocation MGT
    path('api/v1/admin/allocate-room/', AllocationMGT.as_view(),),
    
    
]

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
# urlpatterns = format_suffix_patterns(urlpatterns)
