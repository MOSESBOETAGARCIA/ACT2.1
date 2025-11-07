from django.contrib import admin
from .models import Clientes, Orden, Empleados

admin.site.register(Clientes)
admin.site.register(Orden)
admin.site.register(Empleados)
