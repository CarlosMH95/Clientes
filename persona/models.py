from django.db import models

# Create your models here.
from django.db import models
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=10)
    direccion = models.CharField(max_length=300)
    ocupacion = models.CharField(max_length=30)