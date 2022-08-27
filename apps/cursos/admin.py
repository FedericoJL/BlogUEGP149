from django.contrib import admin
from .models import Cursos, Persona, Imagenes
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PersonaResource(resources.ModelResource):
    class Meta:
        model = Persona

class PersonaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'apellidos', 'dni']
    list_display = ('nombre', 'apellidos', 'dni', 'curso',)
    resource_class = PersonaResource


# Register your models here.

admin.site.register(Cursos)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Imagenes)

