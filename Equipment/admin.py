from django.contrib import admin
from .models import Equipment
from .models import Catagory
# Register your models here.

admin.site.register(Catagory)
admin.site.register(Equipment)
