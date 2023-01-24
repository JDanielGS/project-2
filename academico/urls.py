from django.urls import path, include
from .views import home, RegistrarCurso

urlpatterns = [
    path('', home),
    path('registrarCurso/', RegistrarCurso),
]