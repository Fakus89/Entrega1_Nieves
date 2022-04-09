from dataclasses import field
from functools import partial


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormCliente(forms.Form):
    nombre = forms.CharField(max_length=20) 
    apellido = forms.CharField(max_length=25)
    telefono = forms.IntegerField()
    email = forms.EmailField()


class FormAuto(forms.Form):
    marca =forms.CharField(max_length=15)
    modelo =forms.CharField(max_length=25)
    patente =forms.CharField(max_length=7)
    


class FormProblema(forms.Form):
    inconveniente = forms.CharField(max_length=50)
   


class BusquedaNombre(forms.Form):
    partial_nombre = forms.CharField(label="Buscar por Nombre",max_length=25)


class BusquedaAuto(forms.Form):
    partial_patente = forms.CharField(label="Buscar por Patente",max_length=25)


class BusquedaInconveniente(forms.Form):
    partial_inconveniente = forms.CharField(label="Buscar inconveniente",max_length=50)

class CreacionDeUsuario(UserCreationForm):
    
    email =forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput())
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput())

    class Meta: 
        model= User
        field= ["email","password1","password2"]
        help_test ={ k:"" for k in field }
        {
            "email":"Solo letras, dígitos y @/./+/-/_.",
            "password1": "Su contraseña no puede ser demasiado similar a su otra información personal, debe contener al menos 8 caracteres y su contraseña no puede ser una contraseña de uso común. Su contraseña no puede ser completamente numérica.",
            "password2":"Repita para Verificacion"
        }