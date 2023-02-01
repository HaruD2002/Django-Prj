from django.db import models

from user.models import User
from Equipment.models import Equipment

# Create your models here.


class Request(models.Model):
    '''
        Create user request for equipment connect to 2 table user and equipment
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="User_request")
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date_created = models.DateTimeField(blank=False, auto_now_add=True)
    expect_return_date = models.DateTimeField(blank=True)
    reason = models.TextField(max_length=1000, null=True, blank=True)
    date_return = models.DateTimeField(blank=True, null=True)
    approval = models.IntegerField(default=0)
    approval_admin = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name="Admin_request",
                                       null=True, blank=True)

    class Meta:
        db_table = 'request'

    def __str__(self):
        return "{} request {}".format(self.user, self.equipment)
