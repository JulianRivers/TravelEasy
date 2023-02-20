from django.contrib import admin
from .models import (C_MOLDE, C_TAMANIO, C_TIPO, PAN_Y_PASTELERIA,
                     PISO, TORTA_CREMA, TORTA_FRIA, PRODUCTO)

admin.site.register(C_MOLDE)
admin.site.register(C_TAMANIO)
admin.site.register(C_TIPO)
admin.site.register(PAN_Y_PASTELERIA)
admin.site.register(PISO)
admin.site.register(TORTA_CREMA)
admin.site.register(TORTA_FRIA)
admin.site.register(PRODUCTO)
