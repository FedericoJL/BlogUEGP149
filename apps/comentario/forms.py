from django import forms
from .models import Comentario

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("usuario", "comentario")
        widgets = {
            "usuario": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "usuario-id",
                    "type": "hidden",
                }
            ),
            "comenatrio": forms.Textarea(attrs={"class": "form-control"}),
        }