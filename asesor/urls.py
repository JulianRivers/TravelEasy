from django.urls import path
from . import views

app_name="asesor"
urlpatterns = [
    path('',views.index, name='index'),
    path('inicio', views.inicio, name="inicio")
]