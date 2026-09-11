from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.listar_productos, name='productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<int:producto_id>', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>', views.eliminar_producto, name='eliminar_producto')
]   
