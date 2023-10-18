from django.forms import ModelForm
from django import forms
from .models import User
from django.contrib.auth.forms import PasswordResetForm ,SetPasswordForm
from django.contrib.auth import get_user_model
user = get_user_model()
from django.forms import ValidationError

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='Email address',
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email','class':'form-control'}),)



class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))



class UserSignupForm(ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('name','email', 'company','address',)
        widgets = {
            'name':forms.TextInput(attrs={"class": "form-control", "placeholder":"Your Name e.g 'Akash' "}),
            'email':forms.EmailInput(attrs={"class": "form-control", "placeholder":"Add Your Email Address here @"}),
            'company':forms.TextInput(attrs={"class": "form-control", "placeholder":"Optional"}),
            'address':forms.TextInput(attrs={"class": "form-control", "placeholder":"Optional"}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email Address',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))




from django.contrib.auth.forms import PasswordChangeForm

class CustomPwdChgForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'name': 'old_password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'name': 'new_password1'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'name': 'new_password2'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
