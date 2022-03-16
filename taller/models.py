from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=25)
    telefono = models.IntegerField(max_length=12)
    email = models.EmailField()


class auto(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=25)
    patente = models.IntegerField(max_length=7)
    


class problema(models.Model):
    inconveniente = models.CharField(max_length=50)
    ingreso = models.DateTimeField()
    arreglado = models.BooleanField()
    egreso = models.DateField()
