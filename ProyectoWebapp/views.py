from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    
    return render(request, "ProyectoWebapp/home.html")



def tienda(request):
    
    return render(request, "ProyectoWebapp/tienda.html")

def blog(request):
    
    return render(request, "ProyectoWebapp/blog.html")

def contacto(request):
    
    return render(request, "ProyectoWebapp/contacto.html")