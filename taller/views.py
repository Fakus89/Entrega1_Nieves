
from django.http import HttpResponse
from django.shortcuts import render
from taller.forms import BusquedaAuto, Cliente, Auto, Problema, BusquedaCliente,BusquedaInconveniente



def taller(request):
    return render(request,"taller/taller1.html", {})


def cliente(request):

    if request.method == "POST":
        clientex= Cliente(request.POST)
        if clientex.is_valid():
            datocliente=clientex.cleaned_data
            nuevo_cliente= Cliente(nombre=datocliente["nombre"],apellido=datocliente["apellido"],telefono=datocliente["telefono"],email=datocliente["email"])
            nuevo_cliente.save
            return render(request, "taller/cliente.html",{"nuevo_cliente":nuevo_cliente})
    clientex= Cliente()
    return render(request, "taller/cliente.html",{"clientex": clientex})


def auto(request):
    if request.method == "POST":
        autox= Auto(request.POST)
        if autox.is_valid():
            datoauto=autox.cleaned_data
            nuevo_auto= Auto(marca=datoauto["marca"],modelo=datoauto["modelo"],patente=datoauto["patente"])
            nuevo_auto.save     
            return render(request, "taller/auto_n.html",{"nuevo_auto":nuevo_auto})
    autox= Auto()
    return render(request, "taller/auto_n.html",{"autox": autox})


def problemas(request):

    if request.method == "POST":
        problema= Problema(request.POST)
        if problema.is_valid():
            datoproblema=problema.cleaned_data
            nuevo_problema= Cliente(inconveniete=datoproblema["inconveniete"],ingeso=datoproblema["ingeso"],arreglado=datoproblema["arreglado"])
            nuevo_problema.save     
            return render(request, "taller/arreglos.html",{"nuevo_problema":nuevo_problema})
    problema= Problema
    return render(request, "taller/arreglos.html",{"problemax": problema})

def busqueda_cliente(request):

    dcliente= request.GET.get("partial_cliente", None)
    if cliente is not None:
        Cliente.object.filter(cliente=dcliente)


    buscador1=BusquedaCliente()
    return render(request,"taller/busqueda_cliente.html",{"buscador1":buscador1})

def busqueda_auto(request):
    dauto= request.GET.get("partial_auto", None)
    if cliente is not None:
        Cliente.object.filter(auto=dauto)

    buscador2= BusquedaAuto()
    return render(request,"taller/busqueda_auto.html",{"buscador2":buscador2})


def busqueda_inconveniente(request):
    dinconveniente= request.GET.get("partial_inconveniente", None)
    if cliente is not None:
        Cliente.object.filter(problemas=dinconveniente)

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


