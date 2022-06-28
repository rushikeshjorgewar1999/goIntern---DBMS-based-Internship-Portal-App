from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product

# Create your views here.

def shophome(request):
    p=Product.objects.all()
    x=Product.objects.get(rating__icontains=5)
    context={
        'p':p,
        'x':x,
        
    }
    return render(request,'shop/home.html',context=context)

def product(request,slug):
    prod=Product.objects.filter(slug=slug)
    print(prod)
    context={
        'pd':prod
    }
    return render(request,'shop/product.html',context=context)

def checkout(request):
    return render(request,'shop/checkout.html')