from django.urls import path
from aplicacion import views

urlpatterns = [
    path('crear-vecino/<str:nombre>/<str:apellido>/', views.crear_vecino),
    path('ver-vecinos/', views.ver_vecinos),
    path('', views.index)
]
