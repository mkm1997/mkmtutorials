from django.db import models
from django.contrib.auth.models import User

class employees(models.Model):

    firstname= models.CharField(max_length=10)
    lastname= models.CharField(max_length=10)
    emp_id=models.ImageField()
    def __str__(self):
        return self.firstname
# Create your models here.


class usersignup(models.Model):
    user = models.OneToOneField(User)
    def __str__(self):
        return self.user.username




class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    contactno=models.IntegerField()
    query=models.TextField(max_length=2000)
    def __str__(self):
        return self.name