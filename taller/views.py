from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from taller.forms import NuevoCliente, AutoX, ProblemaX
from taller.models import Cliente


def Taller(request):
    return render(request,"taller/taller1.html", {})

def Cliente_n(request):

    if request.method == "POST":

        formcliente= NuevoCliente()
        nuevo_cliente= Cliente(nombre=request.POST["nombre"],apellido=request.POST["apellido"],telefono=request.POST["telefono"],email=request.POST["email"])
        nuevo_cliente.save()
        return render(request, "taller/cliente.html",{"formcliente":formcliente})
    return render(request, "taller/cliente.html",{})

def Auto_n(request):
    if request.method == "POST":
        auto_x= Auto_n(marca=request.POST["marca"],modelo=request.POST["modelo"],patente=request.POST["patente"])
        auto_x.save()
        return render(request, "taller/auto_n.html",{"auto_x": auto_x})
    return render(request, "taller/auto_n.html",{})

def Problemas(request):
    if request.method == "POST":
        problema_n= Auto_n(inconveniente=request.POST["inconveniente"],ingreso=request.POST["ingreso"],arreglado=request.POST["arreglado"])
        problema_n.save()
        return render(request, "taller/arreglos.html",{"problema_n": problema_n})
    return render(request, "taller/auto_n.html",{})

def About(request):
    return HttpResponse ('''
                            <h1> Pagina en construcción </h1>
                          ''')

def Contact(request):
    return HttpResponse ('''
                            <h1> Pagina en construcción </h1>
                          ''')


