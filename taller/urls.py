from django.urls import path 
from django.contrib.auth.views import LogoutView
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
    
    path("actualizar_cliente/<int:id>/",views.actualizar_cliente, name="actualizar_cliente"),
    path("cliente/borrar/<int:id>/",views.borrar_cliente, name="borrar_cliente"),
    path("detalle/<int:pk>/",views.ClienteDetalle.as_view(), name="datos_cliente"),

    path("autos/",views.ListaAuto.as_view(), name="listasautos"),
    path("autos/borrar/<int:pk>/",views.ListaAuto.as_view(), name="datos_auto"),
    #path("actualizar_autos/<int:pk>/",views.ListaAuto.as_view(), name="datos_cliente")

    path("problemas/",views.ListaArreglo.as_view(), name="listasproblemas"),
    #path("problemas/borrar/<int:pk>/",views.ClienteDetalle.as_view(), name="datos_cliente")
    #path("actualizar_problemas/<int:pk>/",views.ClienteDetalle.as_view(), name="datos_cliente")
    #path(r"^detalle/(?P<pk>\d+)$/",views.ClienteDetalle.as_view(), name="datos_cliente"),

    path("login/",views.login,name="login"),
    path("logout/", LogoutView.as_view(template_name="taller/logout.html"), name="logout"),
    path("registrar/", views.registrar, name="registrar")
]

 