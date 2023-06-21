from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home(request):
    context = {'home' : True}
    return render(request, 'app/index.html', context)

def about(request):
    context = {'about': True}
    return render(request, 'app/about.html', context)

def services(request):
    context = {'services': True}
    return render(request, 'app/services.html', context)
def loginView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        # return redirect('product')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    form = AuthenticationForm()
    return render(request, 'app/login.html', {'form':form})

@login_required
def productList(request):
    products = Product.objects.filter(user=request.user)
    context = {'products' : products}
    return render(request, 'app/productList.html', context)
