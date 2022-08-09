from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

def create_slug(titulo): 
       slug = slugify(titulo)
       qs = Noticia.objects.filter(slug=slug)
       exists = qs.exists()
       if exists:
           slug = "%s-%s" %(slug, qs.first().id)
       return slug

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null = False, blank = False)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length = 250, null = False)
    fecha = models.DateTimeField(auto_now_add=True)
    resumen = models.TextField(null = True)
    texto = RichTextField(null = True)
    activo = models.BooleanField(default = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null = True)
    destacada = models.BooleanField(default = False)
    imagen = models.ImageField(upload_to = 'media/noticia', default = 'media/noticia/default.png')
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.titulo

    def __unicode__(self):
        return self.categoria

    def get_absolute_url(self):
      return reverse('blog_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
         if not self.slug:
            self.slug = create_slug(self.titulo)
         return super().save(*args, **kwargs)
