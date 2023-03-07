from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Equipo, Estadio, Jugador, Avatar

class FormularioEquipos(ModelForm):
    class Meta:
        model = Equipo
        fields = "__all__"
        
class FormularioJugador(ModelForm):
    class Meta:
        model = Jugador
        fields = "__all__"

class FormularioEstadio(ModelForm):
    class Meta:
        model = Estadio
        fields = "__all__"

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

class FormularioAvatar(ModelForm):
       class Meta:
        model = Avatar
        fields = ["imagen"]