from django.shortcuts import render, redirect
from .forms import VehiculoForm
from . import models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission

@permission_required('vehiculo.add_vehiculo')
def add(request):
   if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('index')
   else:
        form = VehiculoForm()
   return render(request, "add.html", {'form': form})

@login_required
def list(request):
    vehiculos = models.Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    for vehiculo in vehiculos:
        if vehiculo.precio < 10000:
            vehiculo.condicion_precio = 'Bajo'
        elif vehiculo.precio >= 10000 and vehiculo.precio < 30000:
            vehiculo.condicion_precio = 'Medio'
        else:
            vehiculo.condicion_precio = 'Alto'
    return render(request, 'list.html', context)
