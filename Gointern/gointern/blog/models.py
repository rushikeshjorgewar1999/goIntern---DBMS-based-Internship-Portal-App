from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    
    def __str__(self):
        return self.name

class post(models.Model):
    pid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now=True)
    views=models.IntegerField(default=0)
    img=models.ImageField(upload_to='media/blog/images',default='')
    slug=models.CharField(max_length=100)
    author=models.ForeignKey(Author,max_length=100,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title 
    
    
class blogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    time=models.DateTimeField(default=now)
    
    def __str__(self):
        return self.comment[0:20]