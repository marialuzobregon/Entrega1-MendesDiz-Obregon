from django.shortcuts import render, redirect
from aplicacion.models import Vecino
from aplicacion.forms import BusquedaFormulario, VecinoFormulario

def index(request):
    
    return render (request, 'aplicacion/index.html')

def crear_vecino(request): 
    
    if request.method == 'POST':
        
        formulario = VecinoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            departamento = data['departamento'] 
            
            vecino = Vecino (nombre=nombre, apellido=apellido, edad = edad, departamento = departamento)
            vecino.save()
        
            return redirect('ver_vecinos')
    
    formulario = VecinoFormulario()

    return render(request, 'aplicacion/crear_vecino.html', {'formulario': formulario})
    
def ver_vecinos(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        vecinos = Vecino.objects.filter(nombre__icontains = nombre)
    else:
        vecinos = Vecino.objects.all()
    
        formulario = BusquedaFormulario()
    
    return render(request, 'aplicacion/ver_vecinos.html', {'vecinos': vecinos, 'formulario': formulario})

def sobre_nosotros(request):
    
    return render (request, 'aplicacion/sobre_nosotros.html')


