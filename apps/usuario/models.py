from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='usuario', default='usuario/default_user.png')

    def get_absolute_url(self):
        return reverse('last_x_posts', args=[str(self.pk)])



class Integrantes(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    cargo= models.CharField(max_length=100, null=True)
    imagen = models.ImageField(upload_to='usuario', default='usuario/user-default.png')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
            return reverse('last_x_posts', args=[str(self.pk)])
        