from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from App_fbhub.models import *
from App_fbhub.forms import *
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth.decorators import login_required 


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

def about(request):
    return render(request, "../templates/sobre_mi.html")

def dummyPage(request):
    return render(request, "../templates/dummy.html")

def agregarItem(request):
    return render(request, "../templates/agregar.html")

def buscar(request):
    return render(request, "../templates/buscar.html")


#Formularios de creación, edición y remoción de objetos
@login_required
def nuevoJugador(request):
    if request.method == "POST":
        crear_jugador = FormularioJugador(request.POST)
        print(crear_jugador)

        if crear_jugador.is_valid():
            data = crear_jugador.cleaned_data
            jugador = Jugador(nombre=data["nombre"], apellido=data["apellido"], pie_fav=data["pie_fav"], posicion=data["posicion"])
            jugador.save()
            return redirect("../Jugadores")
        
    else:
        crear_jugador = FormularioJugador()

    return render(request, "../templates/nuevoJugador.html", {"crear_jugador":crear_jugador})

@login_required
def editarJugador(request, pk):
    jugador = Jugador.objects.get(nombre=pk)
    form = FormularioJugador(instance=jugador)

    if request.method == "POST":
        form = FormularioJugador(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect("../Jugadores")
    
    context = {"form":form}
    return render(request, "../templates/nuevoJugador.html", context)

@login_required
def eliminarJugador(request, pk):
    jugador = Jugador.objects.get(nombre=pk)
    if request.method == "POST":
        jugador.delete()
        return redirect("../Jugadores")
    context = {"object":jugador}
    return render(request, "../templates/eliminarJugador.html", context)

@login_required
def nuevoEquipo(request):
    if request.method == "POST":
        crear_equipo = FormularioEquipos(request.POST)
        print(crear_equipo)

        if crear_equipo.is_valid():
            data = crear_equipo.cleaned_data
            equipo = Equipo(nombre=data["nombre"], cant_jugadores=data["cant_jugadores"], fundacion=data["fundacion"], estadio=data["estadio"], colores=data["colores"])
            equipo.save()
            return redirect("../Equipos")
        
    else:
        crear_equipo = FormularioEquipos()

    return render(request, "../templates/nuevoEquipo.html", {"crear_equipo":crear_equipo})

@login_required
def editarEquipo(request, pk):
    equipo = Equipo.objects.get(nombre=pk)
    form = FormularioEquipos(instance=equipo)

    if request.method == "POST":
        form = FormularioEquipos(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect("../Equipos")
    
    context = {"form":form}
    return render(request, "../templates/nuevoEquipo.html", context)

@login_required
def eliminarEquipo(request, pk):
    equipo = Equipo.objects.get(nombre=pk)
    if request.method == "POST":
        equipo.delete()
        return redirect("../Equipos")
    context = {"object":equipo}
    return render(request, "../templates/eliminarEquipo.html", context)

@login_required
def nuevoEstadio(request):
    if request.method == "POST":
        crear_estadio = FormularioEstadio(request.POST)
        print(crear_estadio)

        if crear_estadio.is_valid():
            data = crear_estadio.cleaned_data
            estadio = Estadio(nombre=data["nombre"], capacidad=data["capacidad"], ubicacion=data["ubicacion"])
            estadio.save()
            return redirect("../Estadios")
        
    else:
        crear_estadio = FormularioEstadio()

    return render(request, "../templates/nuevoEstadio.html", {"crear_estadio":crear_estadio})

@login_required
def editarEstadio(request, pk):
    estadio = Estadio.objects.get(nombre=pk)
    form = FormularioEstadio(instance=estadio)

    if request.method == "POST":
        form = FormularioEstadio(request.POST, instance=estadio)
        if form.is_valid():
            form.save()
            return redirect("../Estadios")
    
    context = {"form":form}
    return render(request, "../templates/nuevoEstadio.html", context)

@login_required
def eliminarEstadio(request, pk):
    estadio = Estadio.objects.get(nombre=pk)
    if request.method == "POST":
        estadio.delete()
        return redirect("../Estadios")
    context = {"object":estadio}
    return render(request, "../templates/eliminarEstadio.html", context)

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



#Logueo y registro  
def user_login(request):
    if request.method =="POST":
        log = AuthenticationForm(request, data = request.POST)

        if log.is_valid():
            usuario = log.cleaned_data.get("username")
            contrasena = log.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contrasena)

            if user is not None:
                login(request, user)
                return render(request, "../templates/inicio.html")
        else:
            messages.error(request, 'Usuario o contraseña errónea')
            
    log = AuthenticationForm()
    return render(request, "../templates/login.html", {"log":log})

def sign_up(request):
    if request.user.is_authenticated == True:
        return redirect("Inicio")
    
    elif request.method == "POST":
        signForm = UserRegisterForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe, por favor elija otro')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email ya utilizado en otra cuenta, por favor seleccione uno distinto')

        elif signForm.is_valid():
            signForm.cleaned_data["username"]
            signForm.save()
            return redirect("Login")
        
    else:
        signForm = UserRegisterForm()

    return render(request, "../templates/registro.html", {"signForm":signForm})

"""@login_required
def user_update(request, pk):
    if request.method =="POST":
"""
