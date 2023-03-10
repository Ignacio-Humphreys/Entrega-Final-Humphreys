from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    cant_jugadores = models.IntegerField()
    fundacion = models.IntegerField()
    estadio = models.CharField(max_length=40)
    colores = models.CharField(max_length=40, default="")
    escudo = models.ImageField(upload_to="fbhub/media", default="fbhub/media/No-Image-Placeholder.jpg")
    def __str__(self):
        return f"Nombre: {self.nombre} - Jugadores: {self.cant_jugadores} - Fundación: {self.fundacion} - Estadio: {self.estadio} - Colores: {self.colores}"

class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    opcion1 = "Izquierdo"
    opcion2 = "Derecho"
    opciones = [(opcion1, "Izquierdo"), (opcion2, "Derecho")]
    pie_fav = models.CharField(max_length=9, choices=opciones, blank=False)
    posicion = models.CharField(max_length=20)
    equipo_act = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="media/", default="media/No-Image-Placeholder.jpg")
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Pie favorito: {self.pie_fav} - Posición: {self.posicion} - Equipo actual: {self.equipo_act}"

class Estadio(models.Model):
    nombre = models.CharField(max_length=40, default="")
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=40)
    equipo = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="media/", default="media/No-Image-Placeholder.jpg")
    def __str__(self):
        return f"Nombre: {self.nombre} - Capacidad: {self.capacidad} - Ubicación: {self.ubicacion} - Equipo: {self.equipo}"
    
class Avatar(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) #Vinculo con el usuario
    imagen = models.ImageField(upload_to="avatares/", null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Comentario(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=True, blank=True, related_name='comentarios')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, null=True, blank=True, related_name='comentarios')
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE, null=True, blank=True, related_name='comentarios')