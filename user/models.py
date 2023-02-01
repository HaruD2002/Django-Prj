'''
    User model
'''
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
        A class represent a user with extra field email and date of birth
    '''
    email = models.EmailField(max_length=200)
    date_of_birth = models.DateField(blank=True, null=True, auto_now_add=False)

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.username
