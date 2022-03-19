from django.urls import path 
from .views import taller, about, contact, cliente, auto, problemas,busqueda_auto,busqueda_cliente,busqueda_inconveniente

urlpatterns = [
    path("taller/", taller ,name="taller"),
    path("abaut/", about, name="about"),
    path("contact", contact, name="contact"),
    path("cliente/", cliente, name="cliente"),
    path("auto/", auto, name="auto"),
    path("problema/", problemas, name="problemas"),
    path("busquedaauto/", busqueda_auto, name="busqueda_auto"),
    path("busquedacliente/", busqueda_cliente, name="busqueda_cliente"),
    path("busquedainconveniente/", busqueda_inconveniente, name="busqueda_inconveniente"),

    
]

 