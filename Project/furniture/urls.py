from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('design/', design, name="design"),
    path('login/', userLogin, name="userLogin"),
    path('register/', userRegister, name="userRegister"),
    path('logout/', userLogout, name="userLogout"),
    path('contact/', contact, name="contact"),
]
