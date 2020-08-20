from django.urls import path
from . import views

urlpatterns=[
   path('',views.home,name='home'),
   path('index.html',views.index,name='index'),
   path('about.html',views.about,name='about'),
   path('contact.html',views.contact,name='contact'),
   path('practice-areas.html',views.practice,name='practise'),
   path('testimonials.html',views.testimonials,name='testimonials'),
   path('login.html',views.login,name='login'),
   path('register.html',views.register,name='register'),
   path('contact',views.contactform,name='contactform'),
   path('book',views.book,name='book'),
   path('register',views.registerform,name='registerform'),
   path('login',views.loginform,name='loginform'),
   path('logout',views.logout,name='logout'),
]