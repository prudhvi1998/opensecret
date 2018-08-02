from django import forms
from django.forms import FileInput

from opensecretapp.models import *

class SignUpForm(forms.Form):
    first_name = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter FirstName'}), )

    last_name = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter LastName'}), )

    email = forms.EmailField(
        max_length=128,
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email ID'}), )

    username = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter UserName'}), )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter Password'}), )

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter UserName'}), )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}), )

class UpdateProfileForm(forms.ModelForm):
    #pro_pic = forms.ImageField(widget=forms.FileInput(attrs={'id': 'customImage'}))
    pro_pic = forms.ImageField(widget=FileInput,required=False)
    class Meta:
        model = OpenSecretUser
        exclude = ['id', 'user', 'friends', 'messages']

class MessageForm(forms.Form):
    message = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Message'}), )