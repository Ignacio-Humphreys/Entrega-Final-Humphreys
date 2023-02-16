from django.http import HttpResponse
from django.shortcuts import render
from App_fbhub.models import *
from App_fbhub.forms import *

# Create your views here.
def inicio(request):
    return render(request, "../templates/inicio.html")

def equipos(request):
    return render(request, "../templates/equipos.html")

def estadios(request):
    return render(request, "../templates/estadios.html")

def jugadores(request):
    return render(request, "../templates/jugadores.html")

def dummyPage(request):
    return render(request, "../templates/dummy.html")

def agregarItem(request):
    return render(request, "../templates/agregar.html")