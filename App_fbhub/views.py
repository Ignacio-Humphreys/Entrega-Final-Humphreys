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
    avatar = Avatar.objects.filter(user=request.user.id)
    return render(request, "../templates/inicio.html", {"url":avatar[0].imagen.url})

def equipos(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    equipos = Equipo.objects.all()
    context = {"equipos":equipos, "url":avatar[0].imagen.url}
    return render(request, "../templates/equipos.html", context)

def estadios(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    estadios = Estadio.objects.all()
    context = {"estadios":estadios, "url":avatar[0].imagen.url}
    return render(request, "../templates/estadios.html", context)

def jugadores(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    jugadores = Jugador.objects.all()
    context = {"jugadores":jugadores, "url":avatar[0].imagen.url}
    return render(request, "../templates/jugadores.html", context)

def about(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    return render(request, "../templates/sobre_mi.html", {"url":avatar[0].imagen.url})

def dummyPage(request):
    return render(request, "../templates/dummy.html")

def agregarItem(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    return render(request, "../templates/agregar.html", {"url":avatar[0].imagen.url})

def buscar(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    return render(request, "../templates/buscar.html", {"url":avatar[0].imagen.url})


#Formularios de creación, edición y remoción de objetos
@login_required
def nuevoJugador(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        crear_jugador = FormularioJugador(request.POST, request.FILES)
        print(crear_jugador)

        if crear_jugador.is_valid():
            data = crear_jugador.cleaned_data
            jugador = Jugador(nombre=data["nombre"], apellido=data["apellido"], pie_fav=data["pie_fav"], posicion=data["posicion"], imagen=data["imagen"])
            jugador.save()
            return redirect("../Jugadores")
        
    else:
        crear_jugador = FormularioJugador()

    return render(request, "../templates/nuevoJugador.html", {"crear_jugador":crear_jugador, "url":avatar[0].imagen.url})

@login_required
def editarJugador(request, pk):
    avatar = Avatar.objects.filter(user=request.user.id)
    jugador = Jugador.objects.get(nombre=pk)
    form = FormularioJugador(instance=jugador)

    if request.method == "POST":
        form = FormularioJugador(request.POST, request.FILES, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect("../Jugadores")
    
    context = {"form":form, "url":avatar[0].imagen.url}
    return render(request, "../templates/nuevoJugador.html", context)

@login_required
def eliminarJugador(request, pk):
    avatar = Avatar.objects.filter(user=request.user.id)
    jugador = Jugador.objects.get(nombre=pk)
    if request.method == "POST":
        jugador.delete()
        return redirect("../Jugadores")
    context = {"object":jugador, "url":avatar[0].imagen.url}
    return render(request, "../templates/eliminarJugador.html", context)

@login_required
def nuevoEquipo(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        crear_equipo = FormularioEquipos(request.POST, request.FILES)
        print(crear_equipo)

        if crear_equipo.is_valid():
            data = crear_equipo.cleaned_data
            equipo = Equipo(nombre=data["nombre"], cant_jugadores=data["cant_jugadores"], fundacion=data["fundacion"], estadio=data["estadio"], colores=data["colores"], escudo=data["escudo"])
            equipo.save()
            return redirect("../Equipos")
        
    else:
        crear_equipo = FormularioEquipos()

    return render(request, "../templates/nuevoEquipo.html", {"crear_equipo":crear_equipo, "url":avatar[0].imagen.url})

@login_required
def editarEquipo(request, pk):
    avatar = Avatar.objects.filter(user=request.user.id)
    equipo = Equipo.objects.get(nombre=pk)
    form = FormularioEquipos(instance=equipo)

    if request.method == "POST":
        form = FormularioEquipos(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect("../Equipos")
    
    context = {"form":form, "url":avatar[0].imagen.url}
    return render(request, "../templates/nuevoEquipo.html", context)

@login_required
def eliminarEquipo(request, pk):
    avatar = Avatar.objects.filter(user=request.user.id)
    equipo = Equipo.objects.get(nombre=pk)
    if request.method == "POST":
        equipo.delete()
        return redirect("../Equipos")
    context = {"object":equipo, "url":avatar[0].imagen.url}
    return render(request, "../templates/eliminarEquipo.html", context)

@login_required
def nuevoEstadio(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        crear_estadio = FormularioEstadio(request.POST, request.FILES)
        print(crear_estadio)

        if crear_estadio.is_valid():
            data = crear_estadio.cleaned_data
            estadio = Estadio(nombre=data["nombre"], capacidad=data["capacidad"], ubicacion=data["ubicacion"], imagen=data["imagen"])
            estadio.save()
            return redirect("../Estadios")
        
    else:
        crear_estadio = FormularioEstadio()

    return render(request, "../templates/nuevoEstadio.html", {"crear_estadio":crear_estadio, "url":avatar[0].imagen.url})

@login_required
def editarEstadio(request, pk):
    avatar = Avatar.objects.filter(user=request.user.id)
    estadio = Estadio.objects.get(nombre=pk)
    form = FormularioEstadio(instance=estadio)

    if request.method == "POST":
        form = FormularioEstadio(request.POST, request.FILES, instance=estadio)
        if form.is_valid():
            form.save()
            return redirect("../Estadios")
    
    context = {"form":form, "url":avatar[0].imagen.url}
    return render(request, "../templates/nuevoEstadio.html", context)

@login_required
def eliminarEstadio(request, pk):
    avatar = Avatar.objects.filter(user=request.user.id)
    estadio = Estadio.objects.get(nombre=pk)
    if request.method == "POST":
        estadio.delete()
        return redirect("../Estadios")
    context = {"object":estadio, "url":avatar[0].imagen.url}
    return render(request, "../templates/eliminarEstadio.html", context)

#Búsqueda en la base de datos
def buscarEquipo(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    return render(request, "../templates/buscarEquipo.html", {"url":avatar[0].imagen.url})

def buscarJugador(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    return render(request, "../templates/buscarJugador.html", {"url":avatar[0].imagen.url})

def buscarEstadio(request):
   avatar = Avatar.objects.filter(user=request.user.id)
   return render(request, "../templates/buscarEstadio.html", {"url":avatar[0].imagen.url})

def buscarItem(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    if request.GET["nombre"]:
        termino = request.GET["nombre"]
        buscar_estadio = Estadio.objects.filter(nombre__icontains=termino)
        buscar_equipo = Equipo.objects.filter(nombre__icontains=termino)
        buscar_jugador = Jugador.objects.filter(nombre__icontains=termino)
        if buscar_estadio:
            return render(request, "../templates/busquedaFinalizada.html", {"buscar_estadio":buscar_estadio, "nombre":termino, "url":avatar[0].imagen.url})
        elif buscar_equipo:
            return render(request, "../templates/busquedaFinalizada.html", {"buscar_equipo":buscar_equipo, "nombre":termino, "url":avatar[0].imagen.url})
        elif buscar_jugador:
            return render(request, "../templates/busquedaFinalizada.html", {"buscar_jugador":buscar_jugador, "nombre":termino, "url":avatar[0].imagen.url})
    else:
        falla = "No se enviaron los datos correctamente"
        return HttpResponse(falla)



#Logueo y registro  
def user_login(request):
    if request.user.is_authenticated == True:
        return redirect("Inicio")
    
    elif request.method =="POST":
        log = AuthenticationForm(request, data = request.POST)

        if log.is_valid():
            usuario = log.cleaned_data.get("username")
            contrasena = log.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contrasena)

            if user is not None:
                login(request, user)
                return redirect("Inicio")
        else:
            messages.error(request, 'Usuario o contraseña errónea')
            
    log = AuthenticationForm()
    return render(request, "../templates/login.html", {"log":log})

def sign_up(request):
    if request.user.is_authenticated == True:
        return redirect("Inicio")
    elif request.method == 'POST':
        signForm = UserRegistrationForm(request.POST, request.FILES)
        if signForm.is_valid():
            signForm.save()
            return redirect('Login')
    else:
        signForm = UserRegistrationForm()
    return render(request, '../templates/registro.html', {'signForm': signForm})

@login_required
def user_update(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    usuario = request.user
    if request.method =="POST":
      form = UserEditForm(request.POST, request.FILES)
      if form.is_valid():
          datos = form.cleaned_data
          usuario.first_name = datos["first_name"]
          usuario.last_name = datos["last_name"]
          usuario.email = datos["email"]
          usuario.password1 = datos["password1"]
          usuario.password2 = datos["password2"]
          usuario.save()
          return redirect("Inicio")
    
    else:
        form = UserEditForm(initial={"first_name":usuario.first_name, "last_name":usuario.last_name, "email":usuario.email})
    

    context = {"form":form, "usuario":usuario, "url":avatar[0].imagen.url}
    return render(request, "../templates/registro.html", context)

@login_required
def agregarAvatar(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        avatarForm = FormularioAvatar(request.POST, request.FILES, instance=request.user)

        if avatarForm.is_valid():
            avatar.delete()
            usuario= User.objects.get(username=request.user)
            avatarForm = Avatar(user=usuario, imagen=avatarForm.cleaned_data["imagen"])
            avatarForm.save()

            return redirect("Inicio")
            
            
    else:
        avatarForm = FormularioAvatar(instance=request.user)
        context = {"avatarForm":avatarForm, "url":avatar[0].imagen.url}
        return render(request, "../templates/avatar.html", context)


