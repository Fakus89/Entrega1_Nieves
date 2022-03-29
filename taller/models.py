from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=25)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Cliente: {self.nombre}, {self.apellido}, n°:{self.id}"



class Auto(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=25)
    patente = models.CharField(max_length=7)
    
    def __str__(self):
        return f"Patente: {self.patente}: {self.marca}, {self.modelo}, n°:{self.id}"


class Problema(models.Model):
    inconveniente = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Problema: {self.inconveniente}"