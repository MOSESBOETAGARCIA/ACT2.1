from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_cafeteria, name='inicio_cafeteria'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('ver_clientes/', views.ver_clientes, name='ver_clientes'),
    path('actualizar_cliente/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('realizar_actualizacion_cliente/<int:id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('borrar_cliente/<int:id>/', views.borrar_cliente, name='borrar_cliente'),
]
