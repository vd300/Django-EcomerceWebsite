from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {
        'no_of_slides': nSlides,
        'range': range(1, nSlides),
        'product': products
    }
    return render(request, 'eshop/index.html', params)

def about(request):
    return render(request, 'eshop/about.html')

def contact(request):
    return render(request, 'eshop/contact.html')

def tacker(request):
    return render(request, 'eshop/tacker.html')

def search(request):
    return render(request, 'eshop/search.html')

def productV(request):
    return render(request, 'eshop/productV.html')

def checkout(request):
    return render(request, 'eshop/checkout.html')

def register(request):
    return render(request, 'eshop/register.html')

def login(request):
    return render(request, 'eshop/login.html')

def cart(request):
    return render(request, 'eshop/cart.html')

def wishlist(request):
    return render(request, 'eshop/wishlist.html')

