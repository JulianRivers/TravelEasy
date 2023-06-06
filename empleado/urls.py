from django.urls import path
from . import views

app_name="empleado"
urlpatterns = [
    path('inicio', views.inicio, name="inicio"),
]

