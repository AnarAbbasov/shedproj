from django.urls import path
from simplepwd import views


urlpatterns = [
    path('test/',views.testview,name='test'),
    path('login/',views.user_login,name='test')
]
