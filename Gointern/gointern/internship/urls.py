from django.urls import path
from . import views

urlpatterns = [
    path('',views.internhome,name='internhome'),
    path('<int:id>',views.internview,name='internview'),
    path('bangalore/',views.bangalore,name='bangalore'),
    path('hyderbad/',views.hyderabad,name='hyderabad'),
    path('chennai/',views.chennai,name='chennai'),
    path('pune/',views.pune,name='pune'),
    path('<str:slug>',views.company,name='company'),
]
