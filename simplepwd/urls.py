from django.urls import path
from simplepwd import views
app_name = 'simplepwd'

urlpatterns = [
    path('test/',views.testview,name='test'),
    path('login/',views.user_login,name='user_login'),
    path('resources/',views.Resource_ListView.as_view()),
     path('add_pwd/',views.Password_CreateView.as_view())
]
