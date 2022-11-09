from django.db import models

# Create your models here.
class Superheroe(models.Model):
    nombre = models.CharField(max_length=100)
    identidad_secreta = models.CharField(max_length=100)
    edad = models.IntegerField()
    planeta_origen = models.CharField(max_length=100)
    poder = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


