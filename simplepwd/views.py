from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import TemplateView,ListView,DetailView
from simplepwd import models
# Create your views here.


def index(request):
    return render(request, "index.html")


def testview(request):

    return HttpResponse("test succeshul")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
        else:
            print("nologin")
            return render(request, "nologin.html")

    return render(request, "login.html")



class Resource_ListView(ListView):
      model=models.Resource
      template_name='resource_detail.html'
      context_object_name='resource_detail'