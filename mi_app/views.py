from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import View, ListView, CreateView, DeleteView
from django.core import serializers
from .models import Autor, Libro, Comentario
from mi_app.forms import AutorForm, LibroForm, ComentarioForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



class LibroListView(ListView):
    model = Libro
    template_name = 'index.html'
    context_object_name = 'libros'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autores'] = Autor.objects.all()
        context['form'] = LibroForm()
        return context

    def post(self, request, *args, **kwargs):
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
   
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')    

class ObtenerAutoresView(ListView):
    model = Autor

    def get(self, request, *args, **kwargs):
        autores = self.get_queryset()
        data = [{'id': autor.id, 'nombre': autor.nombre} for autor in autores]
        return JsonResponse({'data': data})

class ObtenerLibrosView(ListView):
    model = Libro

    def get(self, request, *args, **kwargs):
        libros = self.get_queryset()
        data = []
        for libro in libros:
            comentarios = Comentario.objects.filter(libro=libro)
            comentarios_data = [{'Comentario_id': c.id, 'Comentario': c.comentario, 'Usuario_id': c.usuario.id} for c in comentarios]
            data.append({
                'id': libro.id,
                'titulo': libro.titulo,
                'autor': libro.autor.nombre,
                'lenguaje': libro.lenguaje,
                'publicacion': libro.publicacion,  
                'ventas': libro.ventas,
                'genero': libro.genero,   # Asegúrate de que tu modelo Autor tenga el atributo nombre
                'comentarios': comentarios_data
            })
        return JsonResponse({'data': data})


class AgregarAutorView(CreateView):
    model = Autor
    form_class = AutorForm

    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 'ok'})

    def form_invalid(self, form):
        return JsonResponse({'status': 'error', 'errors': form.errors})

class AgregarLibroView(CreateView):
    model = Libro
    form_class = LibroForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autores'] = Autor.objects.all()  # Asegúrate de importar el modelo Autor
        return context
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 'ok'})

    def form_invalid(self, form):
        return JsonResponse({'status': 'error', 'errors': form.errors})

        
class EliminarAutorView(DeleteView):
    model = Autor
    def post(self, request, *args, **kwargs):
        try:
            self.get_object().delete()
            return JsonResponse({"status": "ok"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

class EliminarLibroView(DeleteView):
    model = Libro
    def post(self, request, *args, **kwargs):
        try:
            self.get_object().delete()
            return JsonResponse({"status": "ok"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

class AgregarComentarioView(View):
    @method_decorator(login_required)
    def post(self, request, libro_id):
        libro = get_object_or_404(Libro, id=libro_id)
        comentario_texto = request.POST.get('comentario')

        if comentario_texto:
            comentario = Comentario.objects.create(
                libro=libro,
                usuario=request.user,
                comentario=comentario_texto
            )
            return JsonResponse({'status': 'ok', 'comentario': str(comentario)})

        return JsonResponse({'status': 'error', 'message': 'Comentario vacío'})

class CargarComentariosView(View):
    @method_decorator(login_required)
    def get(self, request, libro_id):
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'Usuario no autenticado'}, status=403)

        comentarios = Comentario.objects.filter(libro_id=libro_id, usuario=request.user)
        comentarios_data = [
            {'id': comentario.id, 'comentario': comentario.comentario, 'fecha_creacion': comentario.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}
            for comentario in comentarios
        ]
        return JsonResponse({'status': 'ok', 'comentarios': comentarios_data})
    

class EliminarComentarioView(View):
    @method_decorator(login_required)
    @method_decorator(csrf_exempt, name='dispatch')  
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def delete(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)
        if comentario.usuario != request.user:
            return JsonResponse({'status': 'error', 'message': 'No autorizado para eliminar este comentario'}, status=403)
        
        comentario.delete()
        return JsonResponse({'status': 'ok'})
    
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {'user': request.user})       
    
    
    
    
    
"""        
class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
"""
