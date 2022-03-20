
from django.http import HttpResponse
from django.shortcuts import render
from taller.forms import BusquedaAuto, FormCliente, FormAuto, FormProblema, BusquedaCliente,BusquedaInconveniente
from taller.models import Auto, Cliente, Problema


def taller(request):
    return render(request,"taller/taller1.html", {})


def cliente(request):

    if request.method == "POST":
        clientex= FormCliente(request.POST)
        if clientex.is_valid():
            datocliente=clientex.cleaned_data
            nuevo_cliente= Cliente(nombre=datocliente["nombre"],apellido=datocliente["apellido"],telefono=datocliente["telefono"],email=datocliente["email"])
            nuevo_cliente.save
            return render(request, "taller/cliente.html",{"nuevo_cliente":nuevo_cliente})
    clientex= FormCliente()
    return render(request, "taller/cliente.html",{"clientex": clientex})


def auto(request):

    if request.method == "POST":
        autox= FormAuto(request.POST)
        if autox.is_valid():
            datoauto=autox.cleaned_data
            nuevo_auto= Auto(marca=datoauto["marca"],modelo=datoauto["modelo"],patente=datoauto["patente"])
            nuevo_auto.save     
            return render(request, "taller/auto_n.html",{"nuevo_auto":nuevo_auto})
    autox= FormAuto()
    return render(request, "taller/auto_n.html",{"autox": autox})


def problemas(request):

    if request.method == "POST":
        problemax= FormProblema(request.POST)
        if problemax.is_valid():
            datoproblema=problemax.cleaned_data
            nuevo_problema= Problema(inconveniete=datoproblema["inconveniete"],ingeso=datoproblema["ingeso"],arreglado=datoproblema["arreglado"])
            nuevo_problema.save     
            return render(request, "taller/arreglos.html",{"nuevo_problema":nuevo_problema})
    problemax= FormProblema
    return render(request, "taller/arreglos.html",{"problemax": problemax})

def busqueda_cliente(request):

    dcliente= request.GET.get("partial_cliente", None)
    if dcliente is not None:
        FormCliente.object.filter(cliente=dcliente)


    buscador1=BusquedaCliente()
    return render(request,"taller/busqueda_cliente.html",{"buscador1":buscador1})

def busqueda_auto(request):
    dauto= request.GET.get("partial_auto", None)
    if dauto is not None:
        FormAuto.object.filter(auto=dauto)

    buscador2= BusquedaAuto()
    return render(request,"taller/busqueda_auto.html",{"buscador2":buscador2})


def busqueda_inconveniente(request):
    dinconveniente= request.GET.get("partial_inconveniente", None)
    if dinconveniente is not None:
        FormProblema.object.filter(problemas=dinconveniente)

    buscador3=BusquedaInconveniente()
    return render(request,"taller/busqueda_inconveniente.html",{"buscador3":buscador3})


def about(request):
    return HttpResponse ('''
                            <h1> Pagina en construcción </h1>
                          ''')

def contact(request):
    return HttpResponse ('''
                            <h1> Pagina en construcción </h1>
                          ''')


