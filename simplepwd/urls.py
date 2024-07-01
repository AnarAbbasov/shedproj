from django.urls import path
from simplepwd import views
app_name = 'simplepwd'

urlpatterns = [
    path('test/',views.testview,name='test'),
    path('login/',views.user_login,name='user_login')
]
