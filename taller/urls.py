from django.urls import path 
from .views import taller, about, contact, form_cliente, form_auto, form_problemas,busqueda_auto,busqueda_nombre,busqueda_inconveniente

urlpatterns = [ 
    path("taller/", taller ,name="taller"),
    path("abaut/", about, name="about"),
    path("contact", contact, name="contact"),
    path("form_cliente/", form_cliente, name="form_cliente"),
    path("form_auto/", form_auto, name="form_auto"),
    path("form_problemas/", form_problemas, name="form_problemas"),
    path("busqueda_nombre/", busqueda_nombre, name="busqueda_nombre"),
    path("busqueda_auto/", busqueda_auto, name="busqueda_auto"),
    path("busqueda_inconveniente/", busqueda_inconveniente, name="busqueda_inconveniente"),

    
]

 