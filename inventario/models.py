# inventario/models.py
from django.db import models
from django.core.validators import MinValueValidator

class Almacen(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ubicacion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Almacén"
        verbose_name_plural = "Almacenes"

class Producto(models.Model):
    sku = models.CharField(max_length=50, unique=True, verbose_name='SKU')
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100, blank=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre

class StockProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('producto', 'almacen') # Evita duplicados
        verbose_name = 'Stock de Producto'
        verbose_name_plural = 'Stocks de Productos'

    def __str__(self):
        return f'{self.producto.nombre} en {self.almacen.nombre}: {self.cantidad}'

    @property
    def get_estado_stock(self):
        """Devuelve el estado del stock y la clase de Bootstrap correspondiente."""
        if self.cantidad == 0:
            return {'texto': 'Agotado', 'clase': 'danger'}
        elif self.cantidad <= 10: # Lógica para 'Bajo Stock', puedes ajustarla
            return {'texto': 'Bajo Stock', 'clase': 'warning'}
        else:
            return {'texto': 'En Stock', 'clase': 'success'}