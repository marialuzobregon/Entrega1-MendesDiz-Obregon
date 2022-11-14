from django.urls import path
from cuentas import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('registrar', views.registrar, name='registrar'),
    path('salir', LogoutView.as_view(template_name='cuentas/salir.html'), name='salir')
]
