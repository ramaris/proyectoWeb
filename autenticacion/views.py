from tkinter.tix import Form
from urllib.request import Request
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms


# Create your views here.
class VRregistro(View, UserCreationForm):
    
    def get(self, request):
        form=UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})
    
    def post(self, request):
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
        
            usuario=form.save()
            login(request, usuario)
        
            return redirect('home')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, "registro/registro.html", {"form":form})
        
    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
def cerrar_sesion(request):
    logout(request)
    
    return redirect('home')

def loguear(request):
    form=AuthenticationForm()
    
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "Usuario no valido")
    
    return render(request, "login/login.html", {"form":form})
    
