from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name='home'),
    path('cussignup',views.cussignup),
    path('adminlogin',views.adminlogin),
    path('cuslogin',views.cuslogin),
    path('resellerlogin',views.resellerlogin),
    path('master',views.master)


]