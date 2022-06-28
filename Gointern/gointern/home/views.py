from email import message
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import UserManager
from django.contrib import messages
from django.contrib.auth import authenticate
from internship.models import jobposting
from registration.models import company_register
from home.models import Contact
from blog.models import post
# Create your views here.

def home(request):
    job=jobposting.objects.all()[:5]
    j=post.objects.get(title__icontains='django')
    p=post.objects.get(title__icontains='machine')
    r=jobposting.objects.filter(posttitle__exact='Backened Developer')
    s=jobposting.objects.filter(posttitle__exact='operation asscociate')
    context={
        'job':job,
        'j':j,
        'p':p,
        'r':r,
        's':s,
    }
    return render(request,'home/home.html',context=context)

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['conname']
        email=request.POST['conemail']
        subject=request.POST['consubject']
        message=request.POST['conmessage']

        ct=Contact(name=name,email=email,subject=subject,message=message)
        ct.save()

    return render(request,'home/contact.html')

def signup(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        emailid=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['password2']
        
        if len(username) > 10:
            messages.ERROR(request,'enter the only 10 or less characters')
            redirect('home')
        
        if  username.alphanum():
            messages.ERROR(request,'enter only characters')
            redirect('home')
        
        if password!=confirm_password:
            messages.ERROR(request,'enter the correct password')
            redirect('home')
            
        myuser=UserManager.create_user(username=username,email=emailid,password=password)
        myuser.firstname=firstname
        myuser.lastname=lastname
        myuser.save()   
        messages.SUCCESS(request,'congrats ! your are signedUp successfully')
        return redirect('/')
    
    return render(request,'home/signup.html')

def login(request):
    if request.method=='POST':
        logusername=request.POST['loginusername']
        logpassword=request.POST['loginpassword']
        
        user=authenticate(username=logusername,password=logpassword)

        if user is not None:
            login(request,user)
            messages.SUCCESS(request,'logged in successfully')
            return redirect('home')
        else:
            messages.ERROR(request,'enter correct details')
            return redirect('login')

    return render(request,'home/login.html')

def logout(request):
    if request.method=='POST':
        logout(request)
        messages.SUCCESS(request,'successfully logged out')
        return redirect('home')
    else:
        return HttpResponse('404 not found')

def searchintern(request):
    if request.method=='GET':
        role=request.GET['role']
        location=request.GET['location']
        post=jobposting.objects.filter(posttitle__iexact=role)
        city=jobposting.objects.filter(location__icontains=location)
        catpost=jobposting.objects.filter(category__icontains='software  development')
        data=post.union(city)
        count=post.union(city).count()
        context={
            'data':data,
            'count':count,
            'role':role,
            'location':location,
            'catpost':catpost,
            }
    return render(request,'home/internsearch.html',context=context)
                