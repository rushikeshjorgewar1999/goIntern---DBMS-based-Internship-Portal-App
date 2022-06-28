import imp
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from internship.models import  jobposting
from registration.models import company_register

# Create your views here.

def internhome(request):
    return render(request,'internship/internhome.html')

def internview(request,id):
    pt=jobposting.objects.filter(jobid=id).first()
    # print(pt)
    com=company_register.objects.filter(slug=pt)
    context={
        'pt':pt,
        'com':com
    }
    return render(request,'internship/detailview.html',context=context)

def pune(request):
    pun=jobposting.objects.filter(location__icontains='pune')
    context={
        'pun':pun,
    }
    return render(request,'internship/pune.html',context=context)

def bangalore(request):
    chen=jobposting.objects.filter(location__icontains='bangalore')
    context={
        'chen':chen
    }
    return render(request,'internship/bangalore.html',context=context)

def hyderabad(request):
    chen=jobposting.objects.filter(location__icontains='hyderabad')
    context={
        'chen':chen
    }
    return render(request,'internship/hyderabad.html',context=context)

def chennai(request):
    chen=jobposting.objects.filter(location__icontains='chennai')
    context={
        'chen':chen
    }
    return render(request,'internship/chennai.html',context=context)

def company(request,slug):
    pst=company_register.objects.filter(company_name=slug)
    context={
        'p':pst
    }
    return render(request,'internship/company.html',context=context)
