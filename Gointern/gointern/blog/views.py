from pyexpat.errors import messages
from turtle import title
from django.conf import UserSettingsHolder
from django.shortcuts import render,redirect
from django.contrib import messages
from blog.models import post,blogComment,Author

# Create your views here.
def bloghome(request):
    obj=post.objects.all()
    context={
        'obj':obj
    }
    return render(request,'blog/home.html',context=context)


def blogpost(request,slug):
    pt=post.objects.filter(slug=slug).first()
    pt.views=pt.views+1
    pt.save()
    comment=blogComment.objects.filter(post=pt)
    count=blogComment.objects.filter(post=pt).count()
    pst=post.objects.get(title__icontains='django')
    st=post.objects.get(title__icontains='machine')
    context={
        'pt':pt,
        'comments':comment,
        'count':count,
        'user':request.user,
        'pst':pst,
        'st':st,
    }   
    return render(request,'blog/blogpost.html',context=context)

def searchpage(request):
    if request.method=='GET':
        search=request.GET['search']
        if len(search)>30:
            pst=[]
        else:
            postTitle=post.objects.filter(title__icontains=search)
            postContent=post.objects.filter(content__icontains=search)
            allPost=postTitle.union(postContent)
            countPost=postTitle.union(postContent).count()
            ps=post.objects.filter(content__icontains='artificial intelligence')[:2]
        
        context={
            'post':allPost,
            'ps':ps,
            'search':search,
            'count':countPost,
        }
        return render(request,'blog/searchpage.html',context=context)

def postcomment(request):
    if request.method=='POST':
        comment=request.POST.get('comment')
        user=request.user
        sno=request.POST.get('postsno')
        pst=post.objects.get(pid=sno)
        
        comments=blogComment(user=user,comment=comment,post=pst)
        comments.save()
        messages.add_message(request,messages.SUCCESS,'comment posted successfully')

    return redirect('/blog/sno',)
