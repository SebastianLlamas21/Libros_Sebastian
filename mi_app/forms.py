from django import forms
from .models import Libro, Autor, Comentario

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'lenguaje', 'ventas', 'publicacion'] 
        

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre']
        
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['libro', 'comentario']