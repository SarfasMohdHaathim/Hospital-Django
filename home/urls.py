from django.urls import path
from .views import *

urlpatterns = [
    
    path('',home,name='home'),
    path('about',about,name='about'),
    path('doctors',doctors,name='doctors'),
    path('contact',contact,name='contact'),
    path('booking',booking,name='booking'),
    path('department',department,name='department'),
    
]
