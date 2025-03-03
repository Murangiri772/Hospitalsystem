from django.db import models

# Create your models here.

class Patient(models.Model):
    fullname =models.CharField(max_length=1000)
    age=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
      return self.fullname



class Appointment(models.Model):
    name =models.CharField(max_length=50)
    email =models.EmailField()
    phone =models.CharField(max_length=15)
    date =models.DateTimeField()
    department =models.CharField(max_length=50)
    doctor =models.CharField(max_length=50)
    message =models.TextField()


    def __str__(self):
      return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField()
    subject =models.CharField(max_length=50)
    message =models.TextField()

    def __str__(self):
       return self.name
