from mailbox import NoSuchMailboxError
from django import forms

class VecinoFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    departamento = forms.IntegerField()

class BusquedaFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=30, required = False)