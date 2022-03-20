from functools import partial

from django import forms


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
    ingreso = forms.DateTimeField()
    arreglado = forms.BooleanField()


class BusquedaCliente(forms.Form):
    partial_cliente = forms.CharField(label="Buscar",max_length=25)


class BusquedaAuto(forms.Form):
    partial_auto = forms.CharField(label="Buscar",max_length=25)


class BusquedaInconveniente(forms.Form):
    partial_inconveniente = forms.CharField(label="Buscar",max_length=25)