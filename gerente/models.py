from django.db import models

#Modelo Asesor/a
class ASESOR (models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=100)
    telefono = models.CharField('Número de telefono de la asesora', blank=False, unique=True, max_length=15)

    REQUIRED_FIELDS = ['nombre', 'apellido', 'telefono']

    def __str__(self):
        return f"Asesora: {self.nombre} {self.apellido}"

#Modelo Cliente
class CLIENTE (models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=100)
    telefono = models.CharField('Números de telefono del cliente', blank=False, max_length=15)
    direccion = models.CharField('Direccion', max_length=250)

    REQUIRED_FIELDS = ['nombre', 'apellido', 'telefono']

    def __str__(self):
        return f"Cliente: {self.nombre} - tlf: {self.telefono}"