from distutils.command import upload
from django.db import models

# Create your models here.
class Product(models.Model):
    prid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=200)
    pimg=models.ImageField()
    price=models.IntegerField()
    desc=models.TextField()
    color=models.CharField(max_length=100,null=True)
    discount=models.IntegerField()
    select_ppr=[
        ('Paperback','Paperback'),
        ('HardCover','HardCover'),
        ('Audiobook','Audiobook'),
    ]
    select_ct=[
        ('Web Framework','Web Framework'),
        ('Programming Language','Programming Languages'),
        ('CS Subjects','CS Subjects'),
        ('Databases','Databases'),
        ('Exams','Exams'),
    ]
    pub_date=models.DateField(auto_now=True)
    category=models.CharField(choices=select_ct,max_length=100)
    author=models.CharField(max_length=100,default='')
    paperback=models.CharField(max_length=100,choices=select_ppr)
    rating=models.IntegerField(default=0)
    language=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    
    def __str__(self):
        return self.pname 
    
    
# class course(models.Model):
#     cid=models.AutoField(primary_key=True)
#     cname=models.CharField(max_length=100)
    