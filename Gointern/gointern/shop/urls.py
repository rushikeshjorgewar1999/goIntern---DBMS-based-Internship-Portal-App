from unicodedata import name
from shop import views
from django.urls import path

urlpatterns = [
    path('',views.shophome,name='shop'),
    path('<str:slug>',views.product,name='product'),
    path('checkout/',views.checkout,name='checkout')
]
