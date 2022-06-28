
from home import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='myhome'),
    path('about/',views.about,name='habout'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('searchintern/',views.searchintern,name='searchintern'),
]
