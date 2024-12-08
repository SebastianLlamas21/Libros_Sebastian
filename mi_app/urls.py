# urls.py
from django.urls import path
from .views import (
    LibroListView,
    IndexView,
    AboutView,
    ObtenerAutoresView,
    ObtenerLibrosView,
    AgregarAutorView,
    AgregarLibroView,
    EliminarAutorView,
    EliminarLibroView,
    #AgregarComentarioView
)
#from .views import AdminDashboardView, UserDashboardView

urlpatterns = [
    path('', LibroListView.as_view(), name='index'),  # Para la lista de libros en index.html
    path('index/', IndexView.as_view(), name='index_view'),  # Otra vista de index, si es necesario
    path('about/', AboutView.as_view(), name='about_view'),  # Otra vista de about, si es necesario
    path('obtener_autores/', ObtenerAutoresView.as_view(), name='obtener_autores'),  # Para obtener autores
    path('obtener_libros/', ObtenerLibrosView.as_view(), name='obtener_libros'),  # Para obtener libros
    path('agregar_autor/', AgregarAutorView.as_view(), name='agregar_autor'),  # Para agregar un autor
    path('agregar_libro/', AgregarLibroView.as_view(), name='agregar_libro'),  # Para agregar un libro
    path('eliminar_autor/<int:pk>/', EliminarAutorView.as_view(), name='eliminar_autor'),  # Para eliminar un autor
    path('eliminar_libro/<int:pk>/', EliminarLibroView.as_view(), name='eliminar_libro'),  # Para eliminar un libro
    #path('agregar-comentario/', AgregarComentarioView.as_view(), name='agregar_comentario'),
    #path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    #path('user-dashboard/', UserDashboardView.as_view(), name='user_dashboard'),
]