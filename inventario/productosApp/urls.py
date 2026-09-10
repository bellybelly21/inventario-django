from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('productos/', views.listar_productos, name='productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto')
]
