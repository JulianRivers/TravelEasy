from django.db import models

# Catálogo para el tamaño de las tortas
class C_TAMANIO(models.Model):
    tamanio = models.CharField('Tamaño', max_length=15)

    REQUIRED_FIELDS = ['tamanio']

    def __str__(self):
        return f"Tamaño: {self.tamanio}"

# Catálogo para el tipo de torta fría
class C_TIPO (models.Model):
    tipo = models.CharField('Tipo', max_length=50)

    REQUIRED_FIELDS = ['tipo']

    def __str__(self):
        return f"Tipo: {self.tipo}"

# Catálogo para el tipo de molde
class C_MOLDE(models.Model):
    molde = models.CharField('Tipo de molde', max_length=15)

    REQUIRED_FIELDS = ['molde']

    def __str__(self):
        return f"Molde: {self.molde}"

# Modelo de una torta fría
class TORTA_FRIA (models.Model):
    id_tipo = models.ForeignKey(C_TIPO, on_delete=models.CASCADE)
    cubierta = models.CharField('Cubierta', max_length=200)
    mensaje = models.CharField('Mensaje', max_length=250)
    valor = models.FloatField('Precio')

    REQUIRED_FIELDS = ['id_tipo', 'valor']

    def __str__(self):
        return f"tipo torta:{self.id_tipo}, cubierta: {self.cubierta}, mensaje: {self.mensaje}, precio: {self.valor}"

# Modelo de torta crema
class TORTA_CREMA (models.Model):
    id_tamanio = models.ForeignKey(C_TAMANIO, on_delete=models.CASCADE)
    id_molde = models.ForeignKey(C_MOLDE, on_delete=models.CASCADE)
    motivo = models.CharField('Motivo', max_length=60)
    base = models.CharField('Base', max_length=50)
    mensaje = models.CharField('Mensaje', max_length=250)
    valor = models.FloatField('Precio')

    REQUIRED_FIELDS = ['id_tamanio', 'id_molde', 'valor']

    def __str__(self):
        return f"Torta crema - Precio: {self.valor}"

# Modelo de Piso de una torta
class PISO(models.Model):
    id_torta_fria = models.ForeignKey(TORTA_CREMA, on_delete=models.CASCADE)
    numero = models.PositiveSmallIntegerField('Número del piso', default=0)
    cordon = models.CharField('Cordon', max_length=100)
    decoracion = models.CharField('Decoración', max_length=250)

    REQUIRED_FIELDS = ['id_torta_fria', 'numero']

    def __str__(self):
        return f"{self.id_torta_fria}, numero: {self.numero}, cordon: {self.cordon}, decoración: {self.decoracion}"

# Modelo de panes especiales por pedido
class PAN_Y_PASTELERIA (models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    valor = models.FloatField('Precio')

    REQUIRED_FIELDS = ['nombre', 'valor']

    def __str__(self):
        return f"{self.nombre}, Precio: {self.valor}"

# Modelo de supertipo producto
class PRODUCTO(models.Model):
    observ = models.TextField('Observaciones')
    cantidad = models.PositiveSmallIntegerField()
    id_torta_fria = models.ForeignKey(TORTA_FRIA, on_delete=models.CASCADE)
    id_torta_crema = models.ForeignKey(TORTA_CREMA, on_delete=models.CASCADE)
    id_pan_y_past = models.ForeignKey(
        PAN_Y_PASTELERIA, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['observ', 'cantidad']

    def __str__(self):
        str = ''
        if self.id_torta_fria != None:
            str = f"Torta fría - Precio: {self.cantidad}"
        elif self.id_pan_y_past != None:
            str = f"Pan y pastelería - Precio: {self.cantidad}"
        elif self.id_torta_crema != None:
            str = f"Torta crema - Precio: {self.cantidad}"
        return str
