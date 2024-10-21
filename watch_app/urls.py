from django.urls import path 
from watch_app import views
from .models import *



urlpatterns = [
   
   path('',views.register,name='register'),
   path('registration_details',views.registration_details,name='registration_details'),
   path('login',views.login,name='login'),
   path('view_login',views.view_login,name='view_login'),
   path('checkout',views.checkout,name='checkout'),
   path('order',views.order,name='order') ,
   path('success',views.success,name='success'),
   path('contact',views.contact,name='contact'),
   path('view_contact',views.view_contact,name='view_contact'),
   path('user_account',views.user_account,name='user_account'),
   
  
]