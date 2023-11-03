from django import forms
from . models import User

# Login Form
class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'password'}))

# Registration Form
class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150,widget=forms.TextInput({'class':'form-control','placeholder':'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'email'}))
    password = forms.CharField(widget=forms.PasswordInput({'class':'form-control','placeholder':'password'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput({'class':'form-control','placeholder':'confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password','password_confirm']


