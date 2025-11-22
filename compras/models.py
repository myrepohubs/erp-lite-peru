# compras/models.py
from django.db import models

class Proveedor(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    ruc = models.CharField(max_length=11, unique=True, verbose_name='RUC')
    razon_social = models.CharField(max_length=200, verbose_name='Razón Social')
    direccion = models.CharField(max_length=255, blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=8, choices=ESTADO_CHOICES, default='Activo')

    def __str__(self):
        return f"{self.razon_social} ({self.ruc})"

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'