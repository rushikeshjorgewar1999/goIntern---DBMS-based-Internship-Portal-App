from django.urls import path
from . import views
urlpatterns = [
    path('',views.registerhome,name='registerhome'),
    path('companyregister/',views.companyregister,name='companyregister'),
    path('internregister/',views.internregister,name='internregister'),
]
