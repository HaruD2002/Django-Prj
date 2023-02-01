from django import forms
from .models import Request
from django_select2.forms import Select2Widget


class NewRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['equipment', 'expect_return_date',
                  'reason']
        widgets = {
            'equipment': Select2Widget,
            'expect_return_date': forms.DateInput(format=("%Y-%m-%d"),
                                                  attrs={
                                                      'class': 'form-control',
                                                      'placeholder':
                                                          'Select a date',
                                                          'type': 'date'}),
        }
