from django.urls import path
from simplepwd import views
from django.contrib.auth.decorators import login_required  
app_name = 'simplepwd'

urlpatterns = [
    path('test/',views.testview,name='test'),
    path('login/',views.user_login,name='user_login'),
    path('resources/',login_required(views.Resource_ListView.as_view()),name='resource_list'),
     path('password/',login_required(views.Password_ListView.as_view()),name='password_list'),
    path('add_pwd/',login_required(views.Password_CreateView.as_view()),name='create_password'),
    path('add_resource/',login_required(views.Password_Resource.as_view()),name='create_resource')
]
