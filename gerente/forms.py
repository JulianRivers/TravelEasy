from django import forms

from .models import UserProfile

#Formularios

class Login(forms.Form):
    email = forms.CharField(label='Email ', required=True)
    password = forms.CharField(label='Contraseña ', widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
     required=True)
    
class Registro(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'apellidos', 'email', 'departamento', 'password']
        labels = {
            'name': 'Nombres',
            'apellidos': 'Apellidos',
            'email': 'Email',
            'departamento': 'Departamento'
            
        }