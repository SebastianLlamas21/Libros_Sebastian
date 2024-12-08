from django.urls import path
#from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from .views import SignUpView



urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    #path('login/', CustomLoginView.as_view(), name='login'),  # Vista personalizada de login
    #path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),  # Vista para cerrar sesión
]  