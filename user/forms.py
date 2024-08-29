from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm
from django.forms import ModelForm, TextInput

from .models import User, UserGuide

class UserLoginForms(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", 'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
         "class": "form-control py-4", 'placeholder': 'Введите пароль'
    }))
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
    
class UserRegistrationForms(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", 'placeholder': 'Введите имя пользователя'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
         "class": "form-control py-4", 'placeholder': 'Введите адрес эл. почты'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", 'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
         "class": "form-control py-4", 'placeholder': 'Подтвердите пароль'
    }))
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserSetupForm(ModelForm):
    class Meta:
        model = UserGuide
        fields = ['trackName', 'carName', 'pass_time']
        
        # widgets = {
        #     'trackName': TextInput(attrs={
        #         'class': 'setup-track',
        #         'id': 'track'
        #     }),
        #     'carName': TextInput(attrs={
        #         'class': 'setup-car',
        #         'id': 'car'
        #     }),
        #     'pass_time': TextInput(attrs={
        #         'class': 'setup-time',
        #         'id': 'time'
        #     })
        # }
        
        
class ChangePasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })