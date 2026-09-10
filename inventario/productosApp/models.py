from django.db import models

# Create your models here.
# Tabla Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=100);

    def __str__(self):
        return self.nombre;

# Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100);
    precio = models.PositiveIntegerField();
    stock = models.PositiveIntegerField(default=0);
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT);

    def __str__(self):
            return self.nombre;
