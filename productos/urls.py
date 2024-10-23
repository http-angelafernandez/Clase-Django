from django.urls import path 
from productos import views

app_name = 'productos'

urlpatterns = [
    path('cuentos/', views.CrearCuento.as_view(), name='crear_cuento'),
    path('cuentos/crear/', views.ListadoCuentos.as_view(), name='listado_cuentos'),
    path('cuentos/<int:pk>/', views.VerCuento.as_view(), name='ver_cuento'),
    path('cuentos/<int:pk>/editar/', views.EditarCuento.as_view(), name='editar_cuento'),
    path('cuentos/<int:pk>/eliminar/', views.EliminarCuento.as_view(), name='eliminar_cuento')
    ]