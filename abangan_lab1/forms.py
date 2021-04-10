from django import forms
from django.contrib.auth.models import User

class NameForm(forms.Form):
    name = forms.CharField(label='Hello! What is your name?  ',max_length=100)
