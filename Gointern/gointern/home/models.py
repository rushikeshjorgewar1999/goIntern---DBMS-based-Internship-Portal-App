from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()
    
    def __str__(self):
        return 'Message from '+ self.name +'    -   '+ self.email
    
    