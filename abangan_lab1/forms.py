from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Hello! What is your name?  ',max_length=100)