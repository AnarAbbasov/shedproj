from django.db import models
from django.urls import reverse

# Create your models here.

class Resource(models.Model):
    name=models.CharField(max_length=256,unique=True)
    website=models.CharField(max_length=256)
    notes=models.CharField(max_length=256)
    def __str__(self) :
        return str(self.name)
    #what to do if succesful insert to db
    def get_absolute_url(self):
        # Assuming you have a view named 'my_model_detail' that displays details of an instance
       # return reverse('my_model_detail', args=[str(self.id)])
       return reverse('index')

class Passwords(models.Model):
    password=models.CharField(max_length=256)
    username=models.CharField(max_length=256)
    name=models.OneToOneField(Resource, on_delete=models.CASCADE,null=True)
    def __str__(self) :
      return str(self.name)
    def get_absolute_url(self):
        # Assuming you have a view named 'my_model_detail' that displays details of an instance
        #return reverse('my_model_detail', args=[str(self.id)])
      return reverse('index')

