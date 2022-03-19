from django import forms


class NuevoCliente(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=25)
    telefono = forms.IntegerRangeField()
    email = forms.EmailField()


class AutoX(forms.form):
    marca =forms.CharField(max_length=15)
    modelo =forms.CharField(max_length=25)
    patente =forms.IntegerField(max_length=7)
    


class ProblemaX(forms.form):
    inconveniente = forms.CharField(max_length=50)
    ingreso = forms.DateTimeField()
    arreglado = forms.BooleanField()