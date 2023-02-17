from django.http import HttpResponse
from django.shortcuts import render
from App_fbhub.models import *
from App_fbhub.forms import *

# Create your views here.
#Renderizados básicos de páginas
def inicio(request):
    return render(request, "../templates/inicio.html")

def equipos(request):
    equipos = Equipo.objects.all()
    context = {"equipos":equipos}
    return render(request, "../templates/equipos.html", context)

def estadios(request):
    estadios = Estadio.objects.all()
    context = {"estadios":estadios}
    return render(request, "../templates/estadios.html", context)

def jugadores(request):
    jugadores = Jugador.objects.all()
    context = {"jugadores":jugadores}
    return render(request, "../templates/jugadores.html", context)

def dummyPage(request):
    return render(request, "../templates/dummy.html")

def agregarItem(request):
    return render(request, "../templates/agregar.html")

def buscar(request):
    return render(request, "../templates/buscar.html")


#Formularios de creación de objetos
def nuevoJugador(request):
    if request.method == "POST":
        crear_jugador = FormularioJugador(request.POST)
        print(crear_jugador)

        if crear_jugador.is_valid:
            data = crear_jugador.cleaned_data
            jugador = Jugador(nombre=data["nombre"], apellido=data["apellido"], pie_fav=data["pie_fav"], posicion=data["posicion"])
            jugador.save()
            return render(request, "../templates/jugadores.html")
        
    else:
        crear_jugador = FormularioJugador()

    return render(request, "../templates/nuevoJugador.html", {"crear_jugador":crear_jugador})

def nuevoEquipo(request):
    if request.method == "POST":
        crear_equipo = FormularioEquipos(request.POST)
        print(crear_equipo)

        if crear_equipo.is_valid:
            data = crear_equipo.cleaned_data
            equipo = Equipo(nombre=data["nombre"], cant_jugadores=data["cant_jugadores"], fundacion=data["fundacion"], estadio=data["estadio"], colores=data["colores"])
            equipo.save()
            return render(request, "../templates/equipos.html")
        
    else:
        crear_equipo = FormularioEquipos()

    return render(request, "../templates/nuevoEquipo.html", {"crear_equipo":crear_equipo})

def nuevoEstadio(request):
    if request.method == "POST":
        crear_estadio = FormularioEstadio(request.POST)
        print(crear_estadio)

        if crear_estadio.is_valid:
            data = crear_estadio.cleaned_data
            estadio = Estadio(nombre=data["nombre"], capacidad=data["capacidad"], ubicacion=data["ubicacion"])
            estadio.save()
            return render(request, "../templates/estadios.html")
        
    else:
        crear_estadio = FormularioEstadio()

    return render(request, "../templates/nuevoEstadio.html", {"crear_estadio":crear_estadio})

#Búsqueda en la base de datos
def buscarEquipo(request):
    return render(request, "../templates/buscarEquipo.html")

def buscarJugador(request):
    return render(request, "../templates/buscarJugador.html")

def buscarEstadio(request):
   return render(request, "../templates/buscarEstadio.html")

def buscarItem(request):
    if request.GET["nombre"]:
        termino = request.GET["nombre"]
        buscar_estadio = Estadio.objects.filter(nombre__icontains=termino)
        buscar_equipo = Equipo.objects.filter(nombre__icontains=termino)
        buscar_jugador = Jugador.objects.filter(nombre__icontains=termino)
        if buscar_estadio:
            return render(request, "../templates/busquedaFinalizada.html", {"buscar_estadio":buscar_estadio, "nombre":termino})
        elif buscar_equipo:
            return render(request, "../templates/busquedaFinalizada.html", {"buscar_equipo":buscar_equipo, "nombre":termino})
        elif buscar_jugador:
            return render(request, "../templates/busquedaFinalizada.html", {"buscar_jugador":buscar_jugador, "nombre":termino})
    else:
        falla = "No se enviaron los datos correctamente"
        return HttpResponse(falla)
    