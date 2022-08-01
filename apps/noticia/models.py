from django.db import models

# Create your models here.

class Noticias(models.Model):
    titulo = models.CharField(max_length=250, null = False)
    fecha = models.DateTimeField(auto_now = True)
    texto = models.TextField (null = True)
    activo = models.BooleanField( default = True)