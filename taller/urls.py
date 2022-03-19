from django.urls import path 
from .views import Taller, About, Contact, Auto_n, Cliente_n, Problemas

urlpatterns = [
    path("taller/",Taller,name="taller"),
    path("abaut", About, name="about"),
    path("contact", Contact, name="contact"),
    path("auto/" , Auto_n, name="auto"),
    path("cliente/" ,Cliente_n , name="cliente"),
    path("problema/" , Problemas, name="inconveniente"),
    
]

 