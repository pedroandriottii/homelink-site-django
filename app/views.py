from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    context = {'home' : True}
    return render(request, 'app/index.html', context)

def productList(request):
    products = Product
    context = {'products' : products}
    return render(request, 'app/productList.html', context)
