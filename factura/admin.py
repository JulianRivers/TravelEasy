from django.contrib import admin

from django.contrib import admin
from .models import (C_ESTADO, PEDIDO, PRODUCTO_X_PEDIDO )

admin.site.register(C_ESTADO)
admin.site.register(PEDIDO)
admin.site.register(PRODUCTO_X_PEDIDO)
