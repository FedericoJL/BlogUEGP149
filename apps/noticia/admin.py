from django.contrib import admin
from .models import Noticia, Categoria


class NoticiaAdmin(admin.ModelAdmin):
    # con esto añades un campo de texto que te permite realizar la busqueda
    search_fields = ['titulo', 'categoria__nombre']
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display = ('titulo', 'categoria', 'fecha')
    list_filter = ('fecha','destacada')

# Register your models here.

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Categoria)