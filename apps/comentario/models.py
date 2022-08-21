from django.db import models
from django.urls import reverse
from apps.noticia.models import Noticia
from apps.usuario.models import Usuario

# Create your models here.

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comments')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comments', verbose_name='usuario')
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']

    # to make the comment appear with author name and post title
    def __str__(self):
        return self.usuario

# to redirect when adding comment or updating comment 
    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.noticia.pk)])

    