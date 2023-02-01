from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserCreateForm(UserCreationForm):
    'User form'
    first_name = forms.CharField(required=False, max_length=200,
                                 widget=forms.PasswordInput(
                                     attrs={'class': 'form-control mb-3',
                                            'placeholder':
                                            'Enter your first name',
                                            'user-select': 'none',
                                            'id': 'first_name'}))
    last_name = forms.CharField(required=False, max_length=200,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control mb-3',
                                           'placeholder':
                                           'Enter your last name',
                                           'user-select': 'none',
                                           'id': 'last_name'}))
    password1 = forms.CharField(max_length=200,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control mb-3',
                                           'placeholder':
                                           'Enter your password',
                                           'user-select': 'none',
                                           'id': 'password'}))

    password2 = forms.CharField(max_length=200,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control mb-3',
                                           'placeholder':
                                           'Enter your password',
                                           'user-select': 'none',
                                           'id': 'password2'}))

    is_superuser = forms.BooleanField(initial=False,
                                      widget=forms.CheckboxInput(),
                                      required=False)

    is_staff = forms.BooleanField(initial=False,
                                  widget=forms.CheckboxInput(),
                                  required=False)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = 'Enter new password'
        self.fields['password2'].label = 'Re-enter your password'

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name',
                  'email', 'date_of_birth', 'password1',
                  'password2', 'is_superuser', 'is_staff']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder':
                                                   'Enter your username',
                                               'id': 'username'}),

            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'First Name',
                                                 'id': 'first_name',
                                                 'required': True}),

            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Last Name',
                                                'id': 'last_name',
                                                'required': True}),

            'email': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':
                                                'Enter your email'}),

            'date_of_birth': forms.DateInput(format=('%m %d,%y'),
                                             attrs={'class': 'form-control',
                                                    'placeholder':
                                                        'Select a date',
                                                    'type': 'date'}),

            'password1': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'placeholder':
                                                        '''Enter your
                                                        password''',
                                                    'id': 'password',
                                                    'required': True}),

            'password2': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'placeholder':
                                                        '''Re-enter
                                                        your password''',
                                                    'id': 're-password',
                                                    'required': True}),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=200,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control mb-3',
                                          'placeholder': 'Enter your username',
                                          'id': 'username'}))

    password = forms.CharField(max_length=200,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control mb-3',
                                          'placeholder': 'Enter your password',
                                          'id': 'password'}))

    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder':
                '''Enter your username''',
                'id': 'username'}),

            'password': forms.PasswordInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': '''Enter your password''',
                'id': 'password'})
        }


class UpdateUserForm(forms.ModelForm):
    'update the user information'
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", 'email',
                  "date_of_birth"]

        widgets = {
            'date_of_birth': forms.DateInput(format=('%Y-%m-%d'),
                                             attrs={'class': 'form-control',
                                                    'placeholder':
                                                    'Select a date',
                                                    'type': 'date'}),
        }


class AdminUpdateUserForm(forms.ModelForm):
    'update the user information'
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", 'email',
                  "date_of_birth", "is_superuser", "is_staff"]

        widgets = {
            'date_of_birth': forms.DateInput(format=('%Y-%m-%d'),
                                             attrs={'class': 'form-control',
                                                    'placeholder':
                                                    'Select a date',
                                                    'type': 'date'}),
        }


class UserUpdatePasswordForm(forms.ModelForm):
    password1 = forms.CharField(max_length=200,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control mb-3',
                                           'placeholder':
                                           'Enter your password',
                                           'user-select': 'none',
                                           'id': 'password'}))

    password2 = forms.CharField(max_length=200,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control mb-3',
                                           'placeholder':
                                           'Re-enter your password',
                                           'user-select': 'none',
                                           'id': 'password2'}))

    class Meta:
        model = User
        fields = ['password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserUpdatePasswordForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Re-enter your password'
