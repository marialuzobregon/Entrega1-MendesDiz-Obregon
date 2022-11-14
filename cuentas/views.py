from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from cuentas.forms import MiFormularioDeCreacion

def inicio(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            return redirect('index')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'cuentas/inicio.html', {'formulario': formulario})

def registrar(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index') 
    else:
        formulario = MiFormularioDeCreacion()
    
    return render(request, 'cuentas/registrar.html', {'formulario': formulario})