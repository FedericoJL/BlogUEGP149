from django.db import models
from django.urls import reverse

# Create your models here.

class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to = 'curso', default = 'curso/default.png')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
      return reverse('curso', args=[str(self.pk)])
    

class Persona(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellidos = models.CharField(max_length=100, null=False)
    dni = models.BigIntegerField(null=False)
    cuil = models.BigIntegerField(null=True)
    provincia = models.CharField(max_length=100, null=False)
    ciudad = models.CharField(max_length=100, null=False)
    direccion = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    curso = models.ForeignKey(Cursos, on_delete = models.CASCADE,null=True, blank=True)

    def get_absolute_url(self):
      return reverse('curso', args=[str(self.pk)])


class Imagenes(models.Model):
    curso = models.ForeignKey(Cursos,on_delete = models.CASCADE, null=True)
    imagen = models.ImageField(upload_to = 'curso', null=True)
    activo = models.BooleanField(default=True)
    
