from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    ceo = models.CharField(max_length=100)
    est_year = models.IntegerField()
    origin = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo',null=True,blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    seat_capacity = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    cc = models.IntegerField()
    mileage = models.IntegerField()
    price = models.IntegerField()
    product_images = models.ImageField(upload_to='logo',null=True,blank=True)
    company = models.ForeignKey(Company,related_name="companies",on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class ProductInteriorImgs(models.Model):
    interior = models.ImageField(upload_to='interior',null=True,blank=True)
    product = models.ForeignKey(Product,related_name='pii',on_delete=models.CASCADE)

class ProductExteriorImgs(models.Model):
    exterior = models.ImageField(upload_to='exterior',null=True,blank=True)
    product = models.ForeignKey(Product,related_name='pei',on_delete=models.CASCADE)

time_choices = [["9:00-10:00","9:00-10:00"],["10:00-11:00","10:00-11:00"],["11:00-12:00","11:00-12:00"],["12:00-13:00","12:00-13:00"],["14:00-15:00","14:00-15:00"],["15:00-16:00","15:00-16:00"],["16:00-17:00","16:00-17:00"],["17:00-18:00","17:00-18:00"],["18:00-19:00","18:00-19:00"]]

class Time(models.Model):
    time = models.CharField(max_length=100,choices=time_choices)
    date = models.DateField()

class Enquiry(models.Model):
    concern = models.TextField()