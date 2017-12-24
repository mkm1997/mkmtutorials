from django.db import models
from django.contrib.auth.models import User



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