#from django.template import Template, Context
from django.shortcuts import render, HttpResponse
     #carpeta.models import nombre

def Inicio(request):
    return render(request, "ppaginas/Inicio.html")

def Administrador(request):
    return render(request, "ppaginas/signinadmin.html")

def index(request):
    return render(request, "ppaginas/calendario.html")

def Escuelas(request):
    return render(request, "ppaginas/escuelas.html")

def Error(request):
    return render(request, "ppaginas/404.html")