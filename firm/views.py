from django.shortcuts import redirect,render
import firm.models
from django.contrib.auth.models import User,auth
from firm.models import *

def home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def about(request):
    teams=team.objects.all()
    return render(request,'about.html',{'teams':teams})

def contact(request):
    contactin=contactinfo.objects.filter(id=1)
    return render(request,'contact.html',{'contactinfo':contactin})

def practice(request):
    practice1=firm.models.practice.objects.all()
    return render(request,'practice-areas.html',{'practice1':practice1})

def testimonials(request):
    test=firm.models.testimonials.objects.all()
    return render(request,'testimonials.html',{'test':test})

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def contactform(request):
    if(request.method=='POST'):
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        message=request.POST['message']
        contactmessage1=firm.models.contactmessage(fname=fname,lname=lname,email=email,message=message)
        contactmessage1.save()
        print('message sent')
        return redirect("/")
    else:
        return redirect("/")

def book(request):
    if(request.method=='POST'):
      user=request.user
      name=request.POST['name']
      email=request.POST['email']
      date=request.POST['date']
      appointment1=firm.models.appointment(user=user,name=name,email=email,date=date)
      appointment1.save()
      print('booked')
      return redirect("/")
    else:
        return redirect("/")

def registerform(request):
    if(request.method=='POST'):
       username=request.POST['username']
       email=request.POST['email']
       password=request.POST['password']
       password1=request.POST['password1']
       if(password1==password):
        if(User.objects.filter(username=username).exists()==False):
         if(User.objects.filter(email=email).exists()==False):   
          user=User.objects.create_user(username=username,password=password1,email=email)
          user.save()
          print("user added")
          return redirect('/')
         else:
             return render(request,'register.html',{'lol':'email is taken'})
        else:
            return render(request,'register.html',{'lol':'username does exist'})
       else:
           return render(request,'register.html',{'lol':'Passwords are not the same'})
    else:
        return render(request,'index.html')

def loginform(request):
    if(request.method=='POST'):
       username=request.POST['username']
       password=request.POST['password']
       user=auth.authenticate(username=username,password=password)
       if(user is not None):
           auth.login(request,user)
           return redirect('/')
       else:
            return render(request,'login.html',{'lol':"wrong password or username!"})

def logout(request):
    auth.logout(request)
    return redirect('/')