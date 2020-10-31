from django.db import models

# Create your models here.

class Account(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    postalcode = models.CharField(max_length=10)
    about = models.TextField(max_length=300)
    image = models.ImageField(upload_to='profile_picture', blank=True,null=True)