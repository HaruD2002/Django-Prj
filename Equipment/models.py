'''
    model for all the equipment and the request for the equipment of the user
'''
from django.db import models
from django.core.validators import validate_slug


class Catagory(models.Model):
    catagory_id = models.SlugField(verbose_name='Catagory id',
                                   primary_key=True,
                                   max_length=20,
                                   unique=True,
                                   validators=[validate_slug])
    catagory_name = models.CharField(max_length=200, blank=True)
    catagory_definition = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'catagory'

    def __str__(self):
        return self.catagory_id


class Equipment(models.Model):
    '''
        Equipment model
    '''
    equipment_id = models.CharField(verbose_name='Equipment id',
                                    primary_key=True,
                                    unique=True,
                                    blank=False,
                                    max_length=200)
    equipment_name = models.CharField(blank=False, max_length=200)
    equiment_description = models.TextField(blank=True, max_length=9000)
    catagory_id = models.ForeignKey(Catagory,
                                    on_delete=models.CASCADE,
                                    blank=False)
    date_obtained = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        db_table = 'Equipment'

    def __str__(self):
        return self.equipment_name
