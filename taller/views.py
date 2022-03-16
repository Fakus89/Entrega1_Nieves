from django.shortcuts import render


def taller(request):
    return render(request,"taller/taller1.html", {})

