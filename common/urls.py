from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name='home'),
    path('cussignup',views.cussignup),
    path('adminlogin',views.adminlogin),
    path('cuslogin',views.cuslogin),
    path('resellerlogin',views.resellerlogin),
    path('master',views.master),
    path('baabtra',views.baabtra),
    path('tr',views.tr),
    path('grid',views.grid),
    path('grid2',views.grid2)


]