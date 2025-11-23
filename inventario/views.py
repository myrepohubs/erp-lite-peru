from django.shortcuts import render

# Create your views here.

# inventario/views.py
from django.views.generic import ListView
from django.db.models import Sum, F, Value, CharField, DecimalField
from django.db.models.functions import Coalesce
from .models import StockProducto, Almacen, Producto

class ReporteStockView(ListView):
    model = StockProducto
    template_name = 'inventario/stock_actual.html'
    context_object_name = 'stock_items'

    def get_queryset(self):
        queryset = StockProducto.objects.select_related('producto', 'almacen').order_by('producto__nombre')
        
        # Lógica de búsqueda
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(producto__nombre__icontains=query)

        # Lógica de filtro por almacén
        almacen_id = self.request.GET.get('almacen')
        if almacen_id:
            queryset = queryset.filter(almacen__id=almacen_id)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # KPIs
        context['total_productos'] = Producto.objects.count()

        valor_inventario = StockProducto.objects.aggregate(
            total=Coalesce(
                Sum(
                    F('cantidad') * F('producto__precio_compra'),
                    output_field=DecimalField(max_digits=12, decimal_places=2),
                ),
                Value(0, output_field=DecimalField(max_digits=12, decimal_places=2)),
            )
        )['total']

        context['valor_total_inventario'] = valor_inventario
        context['almacenes_activos'] = Almacen.objects.count()
        context['almacenes'] = Almacen.objects.all()

        return context

    def get_template_names(self):
        if 'HX-Request' in self.request.headers:
            return ['inventario/partials/stock_table_partial.html']
        return ['inventario/stock_actual.html']
