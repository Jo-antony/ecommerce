from django.urls import path
from . import views

urlpatterns = [
        
    path('cussignup',views.cussignup),
    path('adminlogin',views.adminlogin, name='adminhome'),
    path('cuslogin',views.cuslogin),
    path('resellerlogin',views.resellerlogin),
    path('master',views.master),
    path('baabtra',views.baabtra, name='baabtra'),
    path('tr',views.tr),
    path('grid',views.grid),
    path('grid2',views.grid2),
    path('grid3',views.grid3),
    path('javascript',views.javascript),
    path('calculator',views.calculator),
    path('jquery',views.jquery),
    path('testing',views.testing),

    






]