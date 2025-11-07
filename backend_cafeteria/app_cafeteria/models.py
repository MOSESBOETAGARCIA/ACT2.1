from django.db import models

# ==========================================
# MODELO: CLIENTES
# ==========================================
class Clientes(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    edad = models.CharField(max_length=10)
    fecha_registro = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    puntos_fidelidad = models.PositiveIntegerField(default=0)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre

# ==========================================

# MODELO: ORDEN
# ==========================================
class Orden(models.Model):
    descripcion = models.CharField(max_length=50)
    numero_orden = models.PositiveIntegerField(unique=True)
    cantidad_items = models.PositiveIntegerField()
    tipo_orden = models.CharField(max_length=30, choices=[
        ('Comida', 'Comida'),
        ('Bebida', 'Bebida'),
        ('Postre', 'Postre')
    ])
    metodo_pago = models.CharField(max_length=30, default='Efectivo')
    completada = models.BooleanField(default=False)
    mesa = models.CharField(max_length=100)
    def __str__(self):
        return f"Orden {self.numero_orden} - {self.tipo_orden}"

# ==========================================
# MODELO: EMPLEADOS
# ==========================================
class Empleados(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    horas_trabajadas = models.PositiveIntegerField(help_text="Horas trabajadas")
    puesto = models.CharField(max_length=10)
    turno = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name="empleados")
    # Relación 1 a muchos: una orden puede tener varios empleados
    clientes = models.ManyToManyField(Clientes, related_name="empleados")
    # Relación muchos a muchos: un empleado puede atender a varios clientes
    def __str__(self):
        return self.nombre
