__author__ = 'lejtman'

from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['receiver', 'subject' ,'content']
