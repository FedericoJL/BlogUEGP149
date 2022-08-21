from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null = False, blank = False)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length = 250, null = False)
    fecha = models.DateTimeField(auto_now_add=True)
    resumen = models.TextField(null = True)
    texto = RichTextField(null = True)
    activo = models.BooleanField(default = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null = True)
    imagen = models.ImageField(upload_to = 'noticia', default = 'noticia/default.png')
   
    class Meta:
        ordering = ['-fecha']
        
    def __str__(self):
        return self.titulo

    def __unicode__(self):
        return self.categoria

    def get_absolute_url(self):
      return reverse('blog_detail', args=[str(self.pk)])

