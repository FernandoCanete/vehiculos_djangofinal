from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio')

    # MARCAS = [
    #     ('Fiat', 'Fiat'),
    #     ('Chevrolet', 'Chevrolet'),
    #     ('Ford', 'Ford'),
    #     ('Toyota', 'Toyota'),
    # ]

    # CATEGORIAS = [
    #     ('Particular', 'Particular'),
    #     ('Transporte', 'Transporte'),
    #     ('Carga', 'Carga'),
    # ]

    # marca = forms.ChoiceField(choices=MARCAS, initial='Ford')
    # modelo = forms.CharField(widget=forms.TextInput)
    # serial_carroceria = forms.CharField(widget=forms.TextInput)
    # serial_motor = forms.CharField(widget=forms.TextInput)
    # categoria = forms.ChoiceField(choices=CATEGORIAS, initial='Particular')
    # precio = forms.FloatField(widget=forms.TextInput)