from django.shortcuts import render, redirect
from .models import curso
from django.contrib import messages

def home(request):
    Cursos=curso.objects.all()
    messages.success(request, '!!Cursos Listados¡¡')
    return render(request, "gestion_cursos.html", {"Cursos": Cursos})

def RegistrarCurso(request):
    codigo=request.POST["txtCOD"]
    nombre=request.POST["txtNOM"]
    creditos=request.POST["txtCRED"]
    messages.success(request, '!!Curso Registrado¡¡')

    Curso=curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)

    return redirect('/')

def EliminarCurso(request, codigo):
    Curso=curso.objects.get(codigo=codigo)
    messages.success(request, '!!Curso Eliminado¡¡')

    Curso.delete()

    return redirect('/')

def EdicionCurso(request, codigo):
    Curso=curso.objects.get(codigo=codigo)
    return render(request, "edicion_curso.html", {"curso":Curso})

def EditarCurso(request):
    codigo=request.POST["txtCOD"]
    nombre=request.POST["txtNOM"]
    creditos=request.POST["txtCRED"]

    Curso=curso.objects.get(codigo=codigo)
    Curso.nombre = nombre
    Curso.creditos = creditos

    Curso.save()
    messages.success(request, '!!Curso Actualizado¡¡')

    return redirect('/')