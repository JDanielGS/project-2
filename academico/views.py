from django.shortcuts import render
from .models import curso

def home(request):
    Cursos=curso.objects.all()
    return render(request, "gestion_cursos.html", {"Cursos": Cursos})