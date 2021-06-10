from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django import forms
from django.db.models import fields
from .models import Works
from .models import Request

from .models import CustomUser
from artgallery import models

# Подклассы форм Изминения и Добавления пользователей
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class RegisterUserForm(CustomUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name','email', 'password1', 'password2')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class AddWorkForm(forms.ModelForm):
    class Meta: 
        model = Works
        fields = ('title', 'description', 'category', 'price', 'photo','autor')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'price': forms.TextInput(attrs={'class': 'form-input'}),
            'photo': forms.FileInput(attrs={'class': 'form-input'}),
            'autor':forms.HiddenInput()
        }




class ChangeLoginForm(CustomUserChangeForm):
    class Meta: 
        model = CustomUser
        fields = ('name', 'email','image','background_image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'bill_number': forms.TextInput(attrs={'class': 'form-input'}),
            'background_image':forms.FileInput(attrs={'class': 'form-input'}),
        }




class AddRequestForm(forms.ModelForm):
    class Meta: 
        model = Request
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={'class': 'form-input'}),
        }

class ImageForm(CustomUserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-input'}),
        }

