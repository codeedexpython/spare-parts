from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brand_images/')

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='vehicle_images/')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='vehicle_brand')

    def __str__(self):
        return self.name
