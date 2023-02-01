"""
    Equipment url paths for view,delete,update equiment for admin
"""
from django.urls import path
from . import views

app_name = 'equipment'

urlpatterns = [
    path(r'view_all_device', views.view_all_equipment,
         name='all_equipment'),

    path(r'delete/<equipment_id>', views.delete_equip,
         name='delete_equipment'),

    path(r'update/<equipment_id>', views.update_equip,
         name='update_equipment'),

    path(r'catagory/view-all', views.view_all_catagory,
         name='view_all_catagory'),

    path(r'catagory/create', views.create_catagory,
         name='create_catagory'),

    path(r'catagory/<catagoryid>/update', views.update_catagory,
         name='update_catagory'),

    path(r'catagory/<catagoryid>/delete', views.delete_catagory,
         name='delete_catagory'),
]
