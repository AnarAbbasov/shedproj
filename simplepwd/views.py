from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.

def index(request):
    return render (request,"index.html")


def testview(request):
    
    
    return HttpResponse("test succeshul")

def user_login(request):
    if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      user=authenticate(username=username,password=password)
      if user:
          if user.is_active:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
    return render(request,"login.html")