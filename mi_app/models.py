from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    lenguaje = models.CharField(max_length=30, default='Desconocido')
    publicacion = models.IntegerField(default=0)
    ventas = models.IntegerField(default=0) 
    genero = models.CharField(max_length=30, default='Desconocido')
    
    def _str_(self):
    	return self.titulo
    
    
class Comentario(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario.username} en {self.libro.titulo}'