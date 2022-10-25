from django.urls import path
from aplicacion import views

urlpatterns = [
    path('crear-vecino/', views.crear_vecino, name = 'crear_vecino'),
    path('ver-vecinos/', views.ver_vecinos, name ='ver_vecinos'),
    path('', views.index, name = 'index'),
    path('sobre-nosotros/', views.sobre_nosotros, name = 'sobre_nosotros')
]
