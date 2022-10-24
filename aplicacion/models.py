from django.db import models

class Vecino(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    edad = models.IntegerField()
    departamento = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    