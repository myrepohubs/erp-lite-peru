# inventario/urls.py
from django.urls import path
from .views import ReporteStockView

app_name = 'inventario'

urlpatterns = [
    path('inventario/stock/', ReporteStockView.as_view(), name='reporte_stock'),
]