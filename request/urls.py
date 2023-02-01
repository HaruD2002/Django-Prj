"""
    Every user also can create a request for an equipment
"""
from django.urls import path
from .views import RequestView
from .views import CurrentReqView
from .views import PreviousReqView
from .views import ReqCreateView
from .views import AdminReqView
from .views import DeleteRequest
from .views import UpdateRequest
from .views import AdminReqView
from .views import AcceptedView
from .views import RejectView
from .views import ReturnView
app_name = 'request'

urlpatterns = [
    path('<username>/request_device',
         RequestView.as_view(template_name='request/request.html'),
         name='my_request_device'),
    path('<username>/current_request',
         CurrentReqView.as_view(template_name='request/current_request.html'),
         name='current_request'),
    path('<username>/previous_request',
         PreviousReqView.as_view(template_name='''
                                 request/previous_request.html'''),
         name='previous_request'),
    path('<username>/request',
         ReqCreateView.as_view(template_name='request/create_request.html'),
         name='create_request'),
    path('admins/request_list',
         AdminReqView.as_view(template_name='request/request_list.html'),
         name='view_request_list'),
    path('admins/<request_id>/request_accepted',
         AcceptedView,
         name='admins_accepted'),
    path('admins/<request_id>/request_rejected',
         RejectView,
         name='admins_rejected'),
    path('request/<request_id>/return',
         ReturnView,
         name='return_device'),
    path('<pk>/delete_request',
         DeleteRequest.as_view(),
         name='delete_request'),
    path('<pk>/update_request',
         UpdateRequest.as_view(template_name='request/update_request.html'),
         name='update_request'),
]
