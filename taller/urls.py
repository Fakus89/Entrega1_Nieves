from django.urls import path 
from .views import Taller,About,Contact, Auto_n, Cliente_n,Problemas

urlpatterns = [
    path("taller/",Taller,name="taller"),
    path("abaut", About, name="about"),
    path("contact", Contact, name="contact"),
    path("taller/auto/" , Auto_n, name="auto"),
    path("taller/cliente/" ,Cliente_n , name="cliente"),
    path("taller/problema/" , Problemas, name="inconveniente"),
    
]

 