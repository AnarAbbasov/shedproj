from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from simplepwd import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CPasswordForm,CResourceForm
from datetime import date
# Create your views here.


def index(request):
    context = {
        'num_posts': date.today,}
    return render(request, "index.html",context=context)


def testview(request):

    return HttpResponse("test succeshul")





class Resource_ListView(LoginRequiredMixin,ListView):
      model=models.Resource
      template_name='resource_detail.html'
      context_object_name='resource_detail'
      login_url='/simplepwd/login/'


class Password_ListView(LoginRequiredMixin,ListView):
      model=models.Passwords
      template_name='password_detail.html'
      context_object_name='password_detail'
      
class Password_CreateView(LoginRequiredMixin,CreateView):
      
      model=models.Passwords
      form_class=CPasswordForm
      template_name='create_password.html'
      #fields=('password','username','name')
      
      
      
    


class Password_Resource(LoginRequiredMixin,CreateView):
      
      model=models.Resource
      form_class=CResourceForm
      template_name='create_resource.html'
      
class Password_SearchView(LoginRequiredMixin,ListView):
      model=models.Resource
      template_name = 'search.html'
      context_object_name = 'resources'
      def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
           return models.Resource.objects.filter(name__icontains=query)
        return ""







      
      
      
      