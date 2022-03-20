from django.urls import path 
from .views import taller, about, contact, form_cliente, form_auto, form_problemas,busqueda_auto,busqueda_cliente,busqueda_inconveniente

urlpatterns = [ 
    path("taller/", taller ,name="taller"),
    path("abaut/", about, name="about"),
    path("contact", contact, name="contact"),
    path("form_cliente/", form_cliente, name="form_cliente"),
    path("form_auto/", form_auto, name="form_auto"),
    path("form_problemas/", form_problemas, name="form_problemas"),
    path("busquedaauto/", busqueda_auto, name="busqueda_auto"),
    path("busquedacliente/", busqueda_cliente, name="busqueda_cliente"),
    path("busquedainconveniente/", busqueda_inconveniente, name="busqueda_inconveniente"),

    
]

 