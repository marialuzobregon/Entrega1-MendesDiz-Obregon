from django.urls import path
from cuentas import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('iniciar/', views.iniciar, name='iniciar'),
    path('registrar/', views.registrar, name='registrar'),
    path('salir/', LogoutView.as_view(template_name='cuentas/salir.html'), name='salir'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-contrasenia/', views.CambiarContrasenia.as_view(), name='cambiar_contrasenia')
]
