from django import forms
from .models import Passwords , Resource


class CPasswordForm(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = ['password', 'username', 'name']
        labels={
            'username':'Benutzername',
            'password': 'Passwort'
        }
        widgets = {
            'password': forms.TextInput(attrs={'class':'form-control'  ,'placeholder':'Passwort'}),
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nutzername',}),
            'name': forms.Select(attrs={'class': 'form-control'}),
        }
        
class CResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'website', 'notes']
        labels={
    'notes':'Notizen',
    'website': 'Webseite'
    }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'  ,'placeholder':'Name'}),
            'website': forms.TextInput(attrs={'class': 'form-control','placeholder':'Webseite'}),
            'notes': forms.TextInput(attrs={'class':'form-control'  ,'placeholder':'Anmerkung'}),
        }