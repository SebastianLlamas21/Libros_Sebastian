from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
"""
class CustomLoginView(LoginView):
    template_name = "registration/login.html"  # Plantilla personalizada para el login

    def form_valid(self, form):
        user = form.get_user()
        if user.is_superuser:
            return redirect('/admin-dashboard/')  # Cambia por la URL de admin_dashboard en mi_app
        else:
            return redirect('/user-dashboard/')  # Cambia por la URL de user_dashboard en mi_app
"""