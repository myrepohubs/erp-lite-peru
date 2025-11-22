# compras/urls.py
from django.urls import path
from .views import ProveedorListView, ProveedorCreateView, ProveedorUpdateView

app_name = 'compras'

urlpatterns = [
    path('proveedores/', ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedores/nuevo/', ProveedorCreateView.as_view(), name='proveedor_create'),
    path('proveedores/<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedor_update'),
    # La URL de borrar se podría añadir aquí
]