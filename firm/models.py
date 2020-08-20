from django.db import models
from django.conf import settings

class appointment(models.Model):
      user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
      name=models.CharField(max_length=40)
      email=models.CharField(max_length=50)
      date=models.CharField(max_length=50)

class practice(models.Model):
      photo=models.ImageField(upload_to='images')
      lawtype=models.CharField(max_length=50)
      text=models.CharField(max_length=100)

class testimonials(models.Model):
      photo=models.ImageField(upload_to='images')
      name=models.CharField(max_length=50)
      company=models.CharField(max_length=50)
      text=models.CharField(max_length=100)

class team(models.Model):
      photo=models.ImageField(upload_to='images')
      name=models.CharField(max_length=50)
      founder=models.CharField(max_length=50)
      text=models.CharField(max_length=100)

class contactmessage(models.Model):
      fname=models.CharField(max_length=50)
      lname=models.CharField(max_length=50)
      email=models.CharField(max_length=50)
      message=models.TextField()

class contactinfo(models.Model):
      address=models.CharField(max_length=50)
      phone=models.CharField(max_length=50)
      email=models.CharField(max_length=50)