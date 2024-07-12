from django.db import models

# Create your models here.

class Resource(models.Model):
    name=models.CharField(max_length=256)
    website=models.CharField(max_length=256)
    notes=models.CharField(max_length=256)
    def __str__(self) :
        return str(self.name)

class Passwords(models.Model):
    password=models.CharField(max_length=256)
    username=models.CharField(max_length=256)
    name=models.OneToOneField(Resource, on_delete=models.CASCADE,null=True)
    def __str__(self) :
      return str(self.name)

