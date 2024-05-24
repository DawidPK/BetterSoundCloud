from django import forms
# from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Add this import statement
from .models import Song  # Add this import statement

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class song_form(forms.Form):
    name = forms.CharField()
    Url = forms.URLField()
    class Meta:
        model = Song
        fields = ["name", "url"]