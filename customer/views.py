from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'customer/home.html')
def cart(request):
    return render(request,'customer/cart.html')
def profile(request):
    return render(request,'customer/profile.html')