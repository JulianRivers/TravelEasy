from django import forms

class Login(forms.Form):
    username = forms.CharField(label='Usuario ', required=True)
    password = forms.CharField(label='Contraseña ', widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
     required=True)