from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

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