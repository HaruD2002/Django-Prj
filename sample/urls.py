from django.contrib import admin
from django.urls import path
from django.urls import include
from user import views as user_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_view.home, name="home"),
    path('', include('user.urls', namespace="user")),
    path('', include('django.contrib.auth.urls')),
    path('equipment/', include('Equipment.urls', namespace="equipment")),
    path("select2/", include("django_select2.urls")),
    path('request/', include('request.urls', namespace="request")),
]
