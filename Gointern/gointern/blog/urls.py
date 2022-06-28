from blog import views
from django.urls import path

urlpatterns = [
    path('postcomment/',views.postcomment,name='postcomment'),
    path('',views.bloghome,name='bloghome'),
    path('search/',views.searchpage,name='searchpage'),
    path('<str:slug>',views.blogpost,name='blogpost'),


]
