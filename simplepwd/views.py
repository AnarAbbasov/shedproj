from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from simplepwd import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
from .forms import CPasswordForm
from datetime import date
# Create your views here.


def index(request):
    context = {
        'num_posts': date.today,}
    return render(request, "index.html",context=context)


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
                #check if its redirect 
                if(str(request.META.get('HTTP_REFERER')).find('=')>0):
                  return HttpResponseRedirect(str(request.META.get('HTTP_REFERER')).split('=')[1])
                else: 
                #direct login page call    
                  return HttpResponseRedirect(reverse('index'))
        else:
            print("nologin")
            return render(request, "nologin.html")

    return render(request, "login.html")



class Resource_ListView(ListView):
      model=models.Resource
      template_name='resource_detail.html'
      context_object_name='resource_detail'
      
class Password_CreateView(CreateView):
      
      model=models.Passwords
      form_class=CPasswordForm
      template_name='create_password.html'
      #fields=('password','username','name')
      @method_decorator(login_required)
      def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)