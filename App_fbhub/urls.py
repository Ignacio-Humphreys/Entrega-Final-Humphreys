from django.urls import path
from App_fbhub import views

urlpatterns = [
    
    path("", views.inicio, name="Inicio"),
    path("Equipos/", views.equipos, name="Equipos"),
    path("Estadios/", views.estadios, name="Estadios"),
    path("Jugadores/", views.jugadores, name="Jugadores"),
    path("Agregar/", views.agregarItem, name="Agregar"),
    path("Dummy/", views.dummyPage, name="Dummy"),    
]