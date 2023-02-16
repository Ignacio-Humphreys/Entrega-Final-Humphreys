from django.urls import path
from App_fbhub import views

urlpatterns = [
    
    path("", views.inicio, name="Inicio"),
    path("Equipos/", views.equipos, name="Equipos"),
    path("Estadios/", views.estadios, name="Estadios"),
    path("Jugadores/", views.jugadores, name="Jugadores"),
    path("Agregar/", views.agregarItem, name="Agregar"),
    path("nuevoEquipo/", views.nuevoEquipo, name="NuevoEquipo"),
    path("nuevoEstadio/", views.nuevoEstadio, name="NuevoEstadio"),
    path("nuevoJugador/", views.nuevoJugador, name="NuevoJugador"),
    path("Buscar/", views.buscar, name="Buscar"), #Página buscar
    path("buscarItem/", views.buscarItem), #Método de búsqueda en views
    path("buscarEquipo/", views.buscarEquipo, name="BuscarEquipo"),
    path("buscarEstadio/", views.buscarEstadio, name="BuscarEstadio"),
    path("buscarJugador/", views.buscarJugador, name="BuscarJugador"),
    path("Dummy/", views.dummyPage, name="Dummy"),    
]