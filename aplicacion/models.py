from django.db import models

class Vecinos(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    edad = models.IntegerField()
    departamento = models.IntegerField()