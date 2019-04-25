from django import forms
from .models import User


class CustomForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'password']
