from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart.html")

def explore(request):
    return render(request, "explore.html")

def account(request):
    return render(request, "account.html")

def product(request):
    return render(request, "product.html")