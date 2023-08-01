from django.contrib import admin
from .models import Vehiculo


class VehiculoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vehiculo, VehiculoAdmin)
