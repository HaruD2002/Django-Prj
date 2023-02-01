'''
    Create for for equipment borrow,
    create new equipment and update equipment information
'''
from django import forms
from .models import Equipment
from .models import Catagory


class CreateEquipment(forms.ModelForm):
    "a form for create new equipment"
    class Meta:
        "form with field id, name and equipment description"
        model = Equipment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateEquipment, self).__init__(*args, **kwargs)
        self.fields['catagory_id'].label = 'Catagory'


class UpdateEquipmentInfo(forms.ModelForm):
    'a form for updating equipment information'
    class Meta:
        'a form with it name and it description'
        model = Equipment
        fields = ['equipment_name', 'equiment_description']


class CreateCatagoryForm(forms.ModelForm):
    catagory_description = forms.TextInput()

    class Meta:
        model = Catagory
        fields = '__all__'


class UpdateCatagoryForm(forms.ModelForm):

    class Meta:
        model = Catagory
        fields = '__all__'
