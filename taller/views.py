
from re import template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BusquedaAuto, FormCliente, FormAuto, FormProblema, BusquedaNombre, BusquedaAuto, BusquedaInconveniente
from .models import Auto, Cliente, Problema
from django.views.generic import ListView


def taller(request):
    return render(request,"taller/taller1.html", {})

def form_cliente(request):

    if request.method == "POST":
        clientex= FormCliente(request.POST)
        if clientex.is_valid():
            datocliente=clientex.cleaned_data
            nuevo_cliente= Cliente(nombre=datocliente["nombre"],apellido=datocliente["apellido"],telefono=datocliente["telefono"],email=datocliente["email"])
            nuevo_cliente.save()
            return render(request, "taller/auto_n.html",{"nuevo_cliente":nuevo_cliente})
    clientex= FormCliente()
    return render(request, "taller/cliente.html",{"clientex": clientex})

def form_auto(request):

    if request.method == "POST":
        autox= FormAuto(request.POST)
        if autox.is_valid():
            datoauto=autox.cleaned_data
            nuevo_auto= Auto(marca=datoauto["marca"],modelo=datoauto["modelo"],patente=datoauto["patente"])
            nuevo_auto.save()     
            return render(request, "taller/arreglos.html",{"nuevo_auto":nuevo_auto})
    autox= FormAuto()
    return render(request, "taller/auto_n.html",{"autox": autox})

def form_problemas(request):

    if request.method == "POST":
        problemax= FormProblema(request.POST)
        if problemax.is_valid():
            datoproblema=problemax.cleaned_data
            nuevo_problema= Problema(inconveniente=datoproblema["inconveniente"])
            nuevo_problema.save()   
            #return render(request, "taller/lista_clientes.html",{"nuevo_problema":nuevo_problema})
    problemax= FormProblema
    return render(request, "taller/arreglos.html",{"problemax": problemax})

##########################################-----busquedas---------########################################

def busqueda_nombre(request):
    nombre_buscado=[]
    dato1=request.GET.get("partial_nombre")
    if dato1 is not None:
        nombre_buscado=Cliente.objects.filter(nombre__icontains=dato1)
    buscador1= BusquedaNombre()
    return render(request, "taller/busqueda_cliente.html", {"buscador1":buscador1,"nombre_buscado":nombre_buscado})


def busqueda_patente(request):
    patente_buscado=[]
    dato2=request.GET.get("partial_patente")
    if dato2 is not None:
        patente_buscado=Auto.objects.filter(patente__icontains=dato2)
    buscador2=BusquedaAuto()
    return render(request, "taller/busqueda_auto.html", {"buscador2":buscador2,"patente_buscado":patente_buscado})

def busqueda_inconveniente(request):
    inconveniente_buscado=[]
    dato3=request.GET.get("partial_inconveniente")
    if dato3 is not None:
        inconveniente_buscado=Problema.objects.filter(inconveniente__icontains=dato3)
    buscador3=BusquedaInconveniente()
    return render(request, "taller/busqueda_inconveniente.html",{"buscador3":buscador3,"inconveniente_buscado":inconveniente_buscado})
#CRUD
#lista de clientes
def lista_clientes(request):
    lista_de_clientes=Cliente.objects.all()
    return render(request,"taller/lista_clientes.html",{"lista_de_clientes":lista_de_clientes})

#actualizar cliente
def actualizar_cliente(request, id):
    cliente=Cliente.objects.get(id=id)

    if request.method == "POST": 
        clientex= FormCliente(request.POST)
        if clientex.is_valid():
            datocliente=clientex.cleaned_data
            cliente.nombre=datocliente["nombre"]
            cliente.apellido=datocliente["apellido"]
            cliente.telefono=datocliente["telefono"]
            cliente.email=datocliente["email"]
            cliente.save()
            return redirect("lista_clientes")
    clientex= FormCliente()
    return render(request, "taller/actualizar_cliente.html",{"clientex": clientex, "cliente":cliente})

#Borrar cliente
def borrar_cliente(request, id):
    cliente=Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("lista_clientes")

#CRUD en BV

class ListaAuto(ListView):
    model=Auto
    template_name="/taller/listas_autos.html"


class ListaArreglo(ListView):
    model= Problema
    template_name="/taller/listas_problemas.html"
##########################################-------para mas adelante-------########################################

def about(request):
    return HttpResponse ('''
                            <h1> Pagina en construcción </h1>
                          ''')

def contact(request):
    return HttpResponse ('''
                            <h1> Pagina en construcción </h1>
                          ''')


