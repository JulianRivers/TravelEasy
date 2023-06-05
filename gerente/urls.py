from django.urls import path
from . import views

app_name="root"
urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.loginView, name='login'),
    path('registro', views.registro, name="registro"),
    path('inicio', views.inicio, name="inicio"),

]