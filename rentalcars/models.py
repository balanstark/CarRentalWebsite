from django.db import models

# Create your models here.

fuel = [
    ('petrol','PETROL'),
    ('diesel','DIESEL'),
    ('ev','EV')
]

no_of_seates = [
    ('5','5'),
    ('7','7')
]

transmission = [
    ('manual','MANUAL'),
    ('automatic','AUTOMATIC')
]

class Carz(models.Model):
    car_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100,choices=fuel)
    seat_capacity = models.CharField(max_length=100, choices=no_of_seates)
    transmission_type = models.CharField(max_length=100,choices=transmission)
    mileage = models.IntegerField()
    total_km_driven = models.IntegerField()
    amminities = models.TextField()
    bootspace = models.IntegerField()
    rating = models.IntegerField()
    carimg = models.ImageField(upload_to="carimg/",null=True,blank=True)

    def __str__(self):
        return self.car_name
    