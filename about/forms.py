# Create form

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    adress = forms.CharField()