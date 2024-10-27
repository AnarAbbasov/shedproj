from django.urls import path
from simplepwd import views
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import views as auth_views
app_name = 'simplepwd'

urlpatterns = [
    path('test/',views.testview,name='test'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logged_out.html'),name='user_logout'),
    path('resources/',views.Resource_ListView.as_view(),name='resource_list'),
    path('password/',views.Password_ListView.as_view(),name='password_list'),
    path('add_pwd/',views.Password_CreateView.as_view(),name='create_password'),
    path('add_resource/',views.Password_Resource.as_view(),name='create_resource'),
    path('search/', views.Password_SearchView.as_view(), name='search'),
    
]
