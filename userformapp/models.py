from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # fields 

    phone = models.IntegerField()
    door_no = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    userpic = models.ImageField(upload_to='userimg/',blank=True,null=True)
