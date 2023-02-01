'''
     User url
'''
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserLoginForm

app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),

    path('login/',
         auth_views.LoginView.as_view(
              template_name="registration/login.html",
              redirect_authenticated_user=True,
              authentication_form=UserLoginForm),
         name="login"),


    path('profile/<username>',
         views.profile,
         name='profile'),

    path('profile/',
         views.user_profile,
         name='user_profile'),


    path('profile/<username>/update',
         views.update_profile,
         name="update_user"),

    path('profile/<username>/update-password',
         auth_views.PasswordChangeView.as_view(
             template_name="registration/password-change-form.html",
             success_url="/profile"),
         name="update_user_password"),

    path('admins/all-user',
         views.all_user,
         name="get_all_users"),

    path('admins/create_user',
         views.create_user,
         name="create_user"),

    path('profile/<username>/delete-user',
         views.delete_user,
         name="delete_user"),

    path('admins/reset-password/<username>',
         views.reset_password,
         name="reset_password"),

    path('admins/ban/<username>',
         views.ban_user,
         name='ban_user'),

    path('admins/unban/<username>',
         views.unban_user,
         name='unban_user'),

    path('search/<username>',
         views.unban_user,
         name='search'),
]
