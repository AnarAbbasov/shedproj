from django import forms
from .models import Passwords


class CPasswordForm(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = ['password', 'username', 'name']
        widgets = {
            'password': forms.TextInput(attrs={'class':'form-control'  ,'placeholder':'Password'}),
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Password'}),
            'name': forms.Select(attrs={'class': 'form-control'}),
        }