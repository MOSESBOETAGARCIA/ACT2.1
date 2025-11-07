from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes

def inicio_cafeteria(request):
    return render(request, 'inicio.html')

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        edad = request.POST.get('edad')
        activo = request.POST.get('activo') == 'on'
        puntos_fidelidad = request.POST.get('puntos_fidelidad')
        avatar = request.POST.get('avatar')
        Clientes.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            edad=edad,
            activo=activo,
            puntos_fidelidad=puntos_fidelidad,
            avatar=avatar
        )
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def ver_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.descripcion = request.POST.get('descripcion')
        cliente.edad = request.POST.get('edad')
        cliente.activo = request.POST.get('activo') == 'on'
        cliente.puntos_fidelidad = request.POST.get('puntos_fidelidad')
        cliente.avatar = request.POST.get('avatar')
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, id):
    return actualizar_cliente(request, id)

def borrar_cliente(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})
