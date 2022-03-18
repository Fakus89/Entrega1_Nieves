from urllib import request
from django.http import HttpResponse
from django.shortcuts import render


def Taller(request):
    return render(request,"taller/taller1.html", {})

def cliente_n(request):
    return render(request, "taller/cliente.html",{})

def auto_n(request):
    return render(request, "taller/auto_n.html",{})

def problemas(request):
    return render(request, "taller/arreglos.html",{})


def About(request):
    return HttpResponse ('''
                            <h1> Pagina en construcción </h1>
                          ''')

def Contact(request):
    return HttpResponse ('''
                            <h1> Pagina en construcción </h1>
                          ''')


