from secrets import choice
from django.db import models

# Create your models here.
class company_register(models.Model):
    cid=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    select_sector=[
        ('I.T','I.T'),
        ('Healthcare','HealthCare'),
        ('Real Estate','Real Estate'),
        ('Ecommerce','Ecommerce'),
        ('Food','Food'),
        ('Space','Space'),
        ('Fintech','Fintech'),
        ('Automobile','Automobile'),
        ('logistics','logistics'),
    ]
    sector=models.CharField(choices=select_sector,max_length=100)
    desc=models.TextField()
    slug=models.CharField(max_length=100,default='')
    size=models.IntegerField(default=0)
    company_email=models.EmailField()
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.company_name
    
class intern_register(models.Model):
    iid=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    iemail=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=300)
    dob=models.DateField()
    deg_level=[
        ('bachelor','bachelor'),
        ('Master','Masters'),
        ('P.HD','P.HD'),
        ('HSC','HSC'),
    ]
    degree=models.CharField(max_length=100,choices=deg_level)
    study_field=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    colleg_city=models.CharField(max_length=100)
    skills=models.CharField(max_length=100)

    def __str__(self):
        return self.fname +'\t'+  self.lname