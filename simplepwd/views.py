from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def index(request):
    return render (request,"index.html")


def testview(request):
    return HttpResponse("test succeshul")

def user_login(request):
    return render(request,"login.html")