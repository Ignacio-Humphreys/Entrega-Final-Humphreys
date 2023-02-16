from django import forms

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