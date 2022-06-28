from unicodedata import category
from django.db import models
from registration.models import company_register

# Create your models here.
class jobposting(models.Model):
    jobid=models.AutoField(primary_key=True)
    posttitle=models.CharField(max_length=100)
    firm=models.ForeignKey(company_register,on_delete=models.CASCADE)
    select_category=[
        ('Software Development','Software Development'),
        ('Marketing','Marketing'),
        ('Testing','Testing'),
        ('Sales & Support','Sales & Support'),
    ]
    select_time=[
        ('Part-time','part-time'),
        ('Full-time','full-time')
        ]
    duration=models.CharField(max_length=100,choices=select_time)
    qualification=models.CharField(max_length=1000,default='')
    category=models.CharField(max_length=100,choices=select_category)
    desc=models.TextField(max_length=2000)
    location=models.CharField(max_length=100)
    stipend=models.IntegerField()
    benefits=models.TextField()
    timeperiod=models.IntegerField()
    
    def __str__(self):
        return  self.posttitle
    
    
    
    
    