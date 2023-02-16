from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    cant_jugadores = models.IntegerField()
    fundacion = models.IntegerField()
    estadio = models.CharField(max_length=40)

class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    pie_fav = models.CharField(max_length=1)
    posicion = models.CharField(max_length=20)

class Estadio(models.Model):
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=40)