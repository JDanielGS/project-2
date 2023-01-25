from django.urls import path, include
from .views import home, RegistrarCurso, EliminarCurso, EdicionCurso, EditarCurso

urlpatterns = [
    path('', home),
    path('registrarCurso/', RegistrarCurso),
    path('eliminarCurso/<codigo>', EliminarCurso),
    path('editarCurso/', EditarCurso),
    path('edicionCurso/<codigo>', EdicionCurso),
]