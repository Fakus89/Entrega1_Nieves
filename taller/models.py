from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=25)
    telefono = models.IntegerField()
    email = models.EmailField()


class Auto(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=25)
    patente = models.CharField(max_length=7)
    


class Problema(models.Model):
    inconveniente = models.CharField(max_length=50)
    ingreso = models.DateTimeField()
    arreglado = models.BooleanField()
    
