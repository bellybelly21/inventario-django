from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productosApp/productos.html', {'productos': productos})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()

    return render(request, 'productosApp/formulario.html', {'form': form, 'titulo': 'Agregar Producto'})


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'productosApp/formulario.html', {'form': form, 'titulo': 'Editar Producto'})


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('productos') 
      
    return render(request, 'productosApp/eliminar.html', {'producto': producto}) 