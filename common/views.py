from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'common/projecthome.html')

def cussignup(request):
    return render(request,'common/cus_signup.html')

def adminlogin(request):
    return render(request,'common/admin_login.html')

def cuslogin(request):
    return render(request,'common/cus_login.html')    

def resellerlogin(request):
    return render(request,'common/reseller_login.html')

def master(request):
    return render(request,'common/master.html')

def baabtra(request):
    return render(request,'common/baabtra.html')

def tr(request):
    return render(request,'common/try.html')

def grid(request):
    return render(request,'common/grid.html')

def grid2(request):
    return render(request,'common/grid2.html')