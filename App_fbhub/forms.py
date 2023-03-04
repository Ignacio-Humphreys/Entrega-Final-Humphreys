from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Equipo, Estadio, Jugador

class FormularioEquipos(forms.Form):
    nombre = forms.CharField(max_length=40)
    cant_jugadores = forms.IntegerField()
    fundacion = forms.IntegerField()
    estadio = forms.CharField(max_length=40)
    colores = forms.CharField(max_length=40)

class FormularioJugador(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    pie_fav = forms.CharField(max_length=1)
    posicion = forms.CharField(max_length=20)

class FormularioEstadio(forms.Form):
    nombre = forms.CharField(max_length=40)
    capacidad = forms.IntegerField()
    ubicacion = forms.CharField(max_length=40)

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField()
    username = forms.CharField(label="Usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]

class UserEditForm(UserCreationForm): #Qué se va a modificar del usuario
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Modificar el email")
    username = forms.CharField(label="Usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetí tu contraseña", widget=forms.PasswordInput)
   

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]