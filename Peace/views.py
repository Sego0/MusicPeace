from django.shortcuts import render
from django.http import HttpResponse

def ini(request):
    return render(request, "prin.html")

def sob(request):
    return render(request, "sobre.html")

def crea(request):
    return render(request, "crea.html")
    
def usu(request):
    return render(request, "usu.html") 

def log(request):
    return render(request, "log.html") 

def reg(request):
    return render(request, "reg.html")               
