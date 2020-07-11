"""Magenta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from django.views import static

from accounts.views import fp,cp,organisation#, register,logout, login

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('login/',login, name="login"),
    #path('register/',register, name="register"),
    path('organisation/',organisation, name="organisation"),
    #path('logout',logout, name="logout"),
    
    path('forgotpass',fp, name="forgotpass"),
    path('changepass',cp, name="changepass"),
    

    path('',include('home.urls'))
]
