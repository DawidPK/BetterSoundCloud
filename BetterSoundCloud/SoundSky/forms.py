from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "password"]
        widgets = {
            'password': forms.PasswordInput(),
        }