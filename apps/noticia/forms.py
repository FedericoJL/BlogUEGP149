from tkinter import Widget
from django import forms
from .models import Noticia, Categoria

choices = Categoria.objects.all().values_list('nombre', 'nombre')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'resumen', 'texto', 'categoria', 'activo', 'imagen')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'activo': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'})
        }
