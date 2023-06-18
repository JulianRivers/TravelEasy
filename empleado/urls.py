from django.urls import path
from . import views

app_name="empleado"
urlpatterns = [
    path('inicio', views.inicio, name="inicio"),
    path('evento/<int:idEvento>', views.evento, name="evento"),
    path('evento/agregar', views.agregarViatico, name="evento"),
]

