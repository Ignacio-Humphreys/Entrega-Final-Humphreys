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
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetí tu contraseña", widget=forms.PasswordInput)
       

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

class FormularioAvatar(forms.ModelForm):
       class Meta:
        model = Avatar
        fields = ["imagen"]
        widgets = {'imagen': forms.FileInput(attrs={'required': True})} #Obligo al usuario a ingresar una imagen para no generar errores
        
class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    imagen = forms.ImageField(label='Avatar', required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
        help_texts = {k: "" for k in fields}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(FormularioAvatar().fields)

    def save(self, commit=True):
        user = super().save(commit=False)
        imagen = self.cleaned_data.get('imagen')
        password = self.cleaned_data.get('password1')
        if commit:
            user.set_password(password)
            user.save()
            if imagen:
                avatar = Avatar(user=user, imagen=imagen)
                avatar.save()
        return user