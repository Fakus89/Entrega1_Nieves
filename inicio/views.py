from django.shortcuts import render

# from django.contrib.auth import login as log, authenticate
# from django.contrib.auth.forms import AuthenticationForm
def inicio(request):
    return render(request,"inicio/index.html", {})


# def login(request):
    
#     #log
#     #authenticate

#     form = AuthenticationForm()
#     return render(request,"inicio/index.html",{"form":form})


