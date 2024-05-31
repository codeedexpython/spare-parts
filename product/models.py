from django.db import models
from django.contrib.auth.models import User
from vehicle.models import Vehicle
# Create your models here.
class Category(models.Model):
    image = models.ImageField(upload_to='category_images/')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ModelYear(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle = models.ManyToManyField(Vehicle, related_name='product_vehicle')
    highlights = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    model_year = models.ForeignKey(ModelYear, on_delete=models.CASCADE, related_name='product_year')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='review_user')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    