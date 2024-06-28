from django.db import models

# Create your models here.

class Resource(models.Model):
    name=models.CharField(max_length=256)
    website=models.CharField(max_length=256)
    notes=models.CharField(max_length=256)

class Passwords(models.Model):
    password=models.CharField(max_length=256)
    username=models.CharField(max_length=256)
    resource=models.ForeignKey(Resource, on_delete=models.CASCADE)

