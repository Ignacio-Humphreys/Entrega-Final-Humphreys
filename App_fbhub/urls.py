from django.urls import path, re_path
from App_fbhub import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("", views.inicio, name="Inicio"),
    path("Equipos/", views.equipos, name="Equipos"),
    path("Estadios/", views.estadios, name="Estadios"),
    path("Jugadores/", views.jugadores, name="Jugadores"),
    path("sobre_mi", views.about, name="About"),
    path("Agregar/", views.agregarItem, name="Agregar"),
    path("nuevoEquipo/", views.nuevoEquipo, name="NuevoEquipo"),
    path("nuevoEstadio/", views.nuevoEstadio, name="NuevoEstadio"),
    path("nuevoJugador/", views.nuevoJugador, name="NuevoJugador"),
    path("editarJugador/<str:pk>", views.editarJugador, name="EditarJugador"),
    path("editarEstadio/<str:pk>", views.editarEstadio, name="EditarEstadio"),
    path("editarEquipo/<str:pk>", views.editarEquipo, name="EditarEquipo"),
    path("eliminarEquipo/<str:pk>", views.eliminarEquipo, name="EliminarEquipo"),
    path("eliminarEstadio/<str:pk>", views.eliminarEstadio, name="EliminarEstadio"),
    path("eliminarJugador/<str:pk>", views.eliminarJugador, name="EliminarJugador"),
    path("comentarios/<str:model>/<str:id>", views.agregar_comentario, name="AgregarComentario"),
    path('eliminar_comentario/<int:pk>/', views.eliminarComentario, name='EliminarComentario'),
    path("Buscar/", views.buscar, name="Buscar"), #Página buscar
    path("buscarItem/", views.buscarItem), #Método de búsqueda en views
    path("buscarEquipo/", views.buscarEquipo, name="BuscarEquipo"),
    path("buscarEstadio/", views.buscarEstadio, name="BuscarEstadio"),
    path("buscarJugador/", views.buscarJugador, name="BuscarJugador"),
    path("Dummy/", views.dummyPage, name="Dummy"),
    path("login", views.user_login, name="Login"),
    path("registro", views.sign_up, name="Register"),
    path("editar", views.user_update, name="Update"),
    path("avatar", views.agregarAvatar, name="Avatar"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
]