from django.shortcuts import render, redirect
from .models import curso

def home(request):
    Cursos=curso.objects.all()
    return render(request, "gestion_cursos.html", {"Cursos": Cursos})

def RegistrarCurso(request):
    codigo=request.POST["txtCOD"]
    nombre=request.POST["txtNOM"]
    creditos=request.POST["txtCRED"]

    Curso=curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)

    return redirect('/')