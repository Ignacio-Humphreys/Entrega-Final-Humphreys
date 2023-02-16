from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    cant_jugadores = models.IntegerField()
    fundacion = models.IntegerField()
    estadio = models.CharField(max_length=40)
    colores = models.CharField(max_length=40, default="")
    def __str__(self):
        return f"Nombre: {self.nombre} - Jugadores: {self.cant_jugadores} - Fundación: {self.fundacion} - Estadio: {self.estadio} - Colores: {self.colores}"

class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    pie_fav = models.CharField(max_length=1)
    posicion = models.CharField(max_length=20)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Pie favorito: {self.pie_fav} - Posición: {self.posicion}"

class Estadio(models.Model):
    nombre = models.CharField(max_length=40, default="")
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.nombre} - Capacidad: {self.capacidad} - Ubicación: {self.ubicacion}"