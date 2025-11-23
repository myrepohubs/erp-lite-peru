# inventario/admin.py
from django.contrib import admin
from .models import Almacen, Producto, StockProducto

admin.site.register(Almacen)
admin.site.register(Producto)
admin.site.register(StockProducto)