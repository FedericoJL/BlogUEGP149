from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null = False, blank = False)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length = 250, null = False)
    fecha = models.DateTimeField(auto_now_add = True)
    texto = RichTextField(null= True)
    activo = models.BooleanField(default = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null = True)
    destacada = models.BooleanField(default = False)
    imagen = models.ImageField(upload_to = 'noticia', default = 'noticia/default.png')

    def __str__(self):
        return self.titulo

    def __unicode__(self):
        return self.categoria