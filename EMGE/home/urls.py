from django.urls import path
from home.views import home,about,partner,companyprofile,terms,dashboard, menapparel

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('partner', partner, name="partner"),
    path('terms', terms, name="terms"),
    path('dashboard',dashboard , name="dashboard"),
    path('companyprofile', companyprofile, name="companyprofile"),
    path('menapparel', menapparel, name="menapparel"),
]
