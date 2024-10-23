from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from inicio.models import Libro
from inicio.forms import CrearLibroFormulario, BuscarLibroFormulario, EditarLibroFormulario
from django.contrib.auth.decorators import login_required

def inicio(request):
    # return HttpResponse('<h1> Soy la pantalla de inicio </h1>')
    return render(request, 'index.html')

def aboutme(request):
    return render(request, 'aboutme.html')
    

def buscar_libro(request):
    formulario = BuscarLibroFormulario(request.GET)
    libros = []  

    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        genero = formulario.cleaned_data.get('genero')
        filters = {}

        if nombre:
            filters['nombre__icontains'] = nombre
        
        if genero: 
            filters['genero__icontains'] = genero

        libros = Libro.objects.filter(**filters)

    return render(request, 'buscar_libro.html', {'libros': libros, 'form': formulario})

@login_required
def crear_libro(request):
   
    print('Request', request)
    print('GET', request.GET) 
    print('POST', request.POST)

    formulario = CrearLibroFormulario()

    if request.method == 'POST':


       formulario = CrearLibroFormulario(request.POST)
       if formulario.is_valid():
           data = formulario.cleaned_data
           libro = Libro(nombre=request.POST.get('nombre'), genero=request.POST.get('genero'), autor=request.POST.get('autor'))
           libro.save()
           return redirect('buscar_libro')
    
    return render(request, 'crear_libro.html', {'form': formulario})

def ver_libro(request, id):
    libro = Libro.objects.get(id=id)
    return render(request, 'ver_libro.html', {'libro': libro})

@login_required
def editar_libro(request, id):
    libro = Libro.objects.get(id=id)

    formulario = EditarLibroFormulario()

    if request.method == "POST":
        formulario = EditarLibroFormulario(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            genero = formulario.cleaned_data.get('genero')
            autor = formulario.cleaned_data.get('autor')

            libro.nombre = nombre
            libro.genero = genero
            libro.autor = autor

            libro.save()

        return redirect('buscar_libro')
    return render(request, 'editar_libro.html', {'libro': libro, 'form': formulario})

@login_required
def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('buscar_libro')




