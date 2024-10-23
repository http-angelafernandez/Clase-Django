from django.urls import path 
from inicio.views import inicio, crear_libro, buscar_libro, aboutme, ver_libro, eliminar_libro, editar_libro

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-libro/<str:nombre>/<str:genero>/<int:autor>/', crear_libro, name='crear_libro'),
    path('buscar-libro/', buscar_libro, name='buscar_libro'),
    path('crear-libro/', crear_libro, name='crear_libro'),
    path('aboutme/', aboutme, name='about_me'),
    path('ver-libro/<int:id>/', ver_libro, name='ver_libro'),
    path('eliminar-libro/<int:id>/', eliminar_libro, name='eliminar_libro'),
    path('editar-libro/<int:id>/', editar_libro, name='editar_libro')


    ]