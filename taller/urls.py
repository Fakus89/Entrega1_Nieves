from django.urls import path 
from . import views 
urlpatterns = [ 
    path("taller/", views.taller ,name="taller"),
    path("abaut/", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("form_cliente/", views.form_cliente, name="form_cliente"),
    path("form_auto/", views.form_auto, name="form_auto"),
    path("form_problemas/", views.form_problemas, name="form_problemas"),

    path("busqueda_nombre/", views.busqueda_nombre, name="busqueda_nombre"),
    path("busqueda_patente/", views.busqueda_patente, name="busqueda_patente"),
    path("busqueda_inconveniente/", views.busqueda_inconveniente, name="busqueda_inconveniente"),

    path("lista_clientes/",views.lista_clientes, name= "lista_clientes"),
    # path("cliente/",views.cliente, name="cliente"),
    # path("cliente/borrar",views.borrar_cliente, name="borrar_cliente"),
    path("taller/actualizar_cliente/<int:id>",views.actualizar_cliente, name="actualizar_cliente"),
]

 