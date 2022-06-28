from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def registerhome(request):
    return HttpResponse('we are in register home page')

def companyregister(request):
    return HttpResponse('we are in register company page')

def internregister(request):
    return HttpResponse('we are in register intern page')