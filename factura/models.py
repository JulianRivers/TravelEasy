from django.db import models
from producto.models import (PRODUCTO)
from asesor.models import(ASESOR, CLIENTE)

#Catálogo de estados de una fáctura
class C_ESTADO(models.Model):
    estado = models.CharField('Estado del pedido', max_length=15)

    REQUIRED_FIELDS = ['estado']
    
    def __str__(self):
        return f"Estado del pedido: {self.estado}"

#Modelo de factura
class PEDIDO(models.Model):
    id_asesor = models.ForeignKey(ASESOR, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(CLIENTE, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(C_ESTADO, on_delete=models.CASCADE)
    fecha_recibido = models.DateTimeField('Fecha de Recibido', auto_now_add=True)
    fecha_entrega = models.DateTimeField('Fecha de Recibido', auto_now_add=False)
    valor_total = models.FloatField('Precio Final')

    REQUIRED_FIELDS = ['id_asesor', 'id_cliente', 'id_estado', 'fecha_entrega', 'valor_total']

    def __str__(self):
        return f"Pedido: {self.id} - Valor total: {self.valor_total}"

class PRODUCTO_X_PEDIDO(models.Model):
    id_producto = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(PEDIDO, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['tamanio']

    def __str__(self):
        return f"Pedido: {self.id_producto},  del Pedido: {self.id_pedido}"