from . import views
from django.urls import path

urlpatterns = [
    path("",views.hello,name="welcome message"),
    
    path("auth/register",views.RegistrationAPIView.as_view(), name="register"), # METHOD : (POST) 
    path("auth/login",views.LoginAPIView.as_view(), name="login"),              # METHOD : (POST)
    path("auth/logout",views.LogoutAPIView.as_view(), name="logout"),           # METHOD : (POST)
    
    
]
