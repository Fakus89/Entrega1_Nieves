from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=25)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"N° de ID:{self.id}, Cliente: {self.nombre}, {self.apellido} "



class Auto(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=25)
    patente = models.CharField(max_length=7)
    
    def __str__(self):
        return f"N° de ID:{self.id}, Patente: {self.patente}, Marca:{self.marca}, Modelo:{self.modelo}"


class Problema(models.Model):
    inconveniente = models.CharField(max_length=50)
    
    def __str__(self):
        return f"N° de ID:{self.id}, Problema: {self.inconveniente}"


class MiAvatarUser(models.Model):

    img = models.ImageField(upload_to="avatares", null = True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
