from django.urls import path 
from .views import Taller,About,Contact, auto_n, cliente_n,formulario_cliente,formulario_auto,formulario_problema, problemas

urlpatterns = [
    path("taller/",Taller,name="taller"),
    path("abaut", About, name="about"),
    path("contact", Contact, name="contact"),
    path("auto/" , auto_n, name="auto nuevo"),
    path("cliente/" ,cliente_n , name="cliente"),
    path("cliente/" , problemas, name="inconveniente"),
    
]

 