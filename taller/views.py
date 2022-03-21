
from django.http import HttpResponse
from django.shortcuts import render
from .forms import BusquedaAuto, FormCliente, FormAuto, FormProblema, BusquedaNombre,BusquedaInconveniente
from .models import Auto, Cliente, Problema


def taller(request):
    return render(request,"taller/taller1.html", {})


def form_cliente(request):

    if request.method == "POST":
        clientex= FormCliente(request.POST)
        if clientex.is_valid():
            datocliente=clientex.cleaned_data
            nuevo_cliente= Cliente(nombre=datocliente["nombre"],apellido=datocliente["apellido"],telefono=datocliente["telefono"],email=datocliente["email"])
            nuevo_cliente.save()
            return render(request, "taller/cliente.html",{"nuevo_cliente":nuevo_cliente})
    clientex= FormCliente()
    return render(request, "taller/cliente.html",{"clientex": clientex})


def form_auto(request):

    if request.method == "POST":
        autox= FormAuto(request.POST)
        if autox.is_valid():
            datoauto=autox.cleaned_data
            nuevo_auto= Auto(marca=datoauto["marca"],modelo=datoauto["modelo"],patente=datoauto["patente"])
            nuevo_auto.save()     
            return render(request, "taller/auto_n.html",{"nuevo_auto":nuevo_auto})
    autox= FormAuto()
    return render(request, "taller/auto_n.html",{"autox": autox})


def form_problemas(request):

    if request.method == "POST":
        problemax= FormProblema(request.POST)
        if problemax.is_valid():
            datoproblema=problemax.cleaned_data
            nuevo_problema= Problema(inconveniete=datoproblema["inconveniete"],ingeso=datoproblema["ingeso"],arreglado=datoproblema["arreglado"])
            nuevo_problema.save()   
            return render(request, "taller/arreglos.html",{"nuevo_problema":nuevo_problema})
    problemax= FormProblema
    return render(request, "taller/arreglos.html",{"problemax": problemax})

##########################################-----busquedas---------########################################3




def busqueda_nombre(request):
    dato1=[]
    dcliente= request.GET.get("partial_nombre", None)
    if dcliente is not None:
        dato1 = Cliente.object.filter(nombre__icontains=dcliente)
    buscador1=BusquedaNombre()
    return render(request,"taller/busqueda_cliente.html",{"buscador1": buscador1 ,"dato1": dato1})


def busqueda_auto(request):
    dato2=[]
    dauto= request.GET.get("partial_auto", None)
    if dauto is not None:
        dato2=Auto.object.filter(auto=dauto)
    buscador2= BusquedaAuto()
    return render(request,"taller/busqueda_auto.html",{"buscador2":buscador2, "dato2": dato2})


def busqueda_inconveniente(request):
    dato3=[]
    dinconveniente= request.GET.get("partial_inconveniente", None)
    if dinconveniente is not None:
        dato3=Problema.object.filter(problemas=dinconveniente)

    buscador3=BusquedaInconveniente()
    return render(request,"taller/busqueda_inconveniente.html",{"buscador3":buscador3,"dato3": dato3})


def about(request):
    return HttpResponse ('''
                            <h1> Pagina en construcción </h1>
                          ''')

def contact(request):
    return HttpResponse ('''
                            <h1> Pagina en construcción </h1>
                          ''')


