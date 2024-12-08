from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View, ListView, CreateView, DeleteView
from django.core import serializers
from .models import Autor, Libro
from mi_app.forms import AutorForm, LibroForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
   
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
        data = [
            {
                'id': libro.id,
                'titulo': libro.titulo,
                'autor': libro.autor.nombre,
                'lenguaje': libro.lenguaje,  # Incluye el nuevo atributo 'lenguaje'
                'publicacion': libro.publicacion,  
                'ventas': libro.ventas,  # Incluye el nuevo atributo 'ventas'
                'genero': libro.genero 
            }
            for libro in libros
        ]
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

"""        
class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
"""
