from django.db import models
from django.urls import reverse

class Vehiculo(models.Model):
    MARCAS = (
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    )
    CATEGORIAS = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    )

    marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.FloatField()
    fecha_de_creacion = models.DateField(auto_now_add=True)
    fecha_de_modificacion = models.DateField(auto_now=True)

    def get_absoluted_url(self):
        return reverse('vehiculo', args=[str(self.id)])

    def __str__(self):
        return f"marca: {self.marca}, modelo: {self.modelo} fecha_creacion: {self.fecha_de_creacion}, fecha_modificacion: {self.fecha_de_modificacion}"
