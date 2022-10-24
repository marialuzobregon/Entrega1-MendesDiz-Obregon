from django.shortcuts import render
from aplicacion.models import Vecinos
import random

def index(request):
    
    return render (request, 'aplicacion/index.html')

def crear_vecino(request, nombre, apellido): 
    
    vecino = Vecinos (nombre = nombre, apellido = apellido, edad = random.randrange(1, 99), departamento = random.randrange(0,21))
    vecino.save()

    return render(request, 'aplicacion/crear_vecino.html', {'vecino': vecino})
    
def ver_vecinos(request):
    
    vecinos = Vecinos.objects.all()
    
    return render(request, 'aplicacion/ver_vecinos.html', {'vecinos': vecinos})