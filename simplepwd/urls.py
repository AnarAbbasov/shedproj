from django.urls import path
from simplepwd import views


urlpatterns = [
    path('',views.index,name='index')
]
