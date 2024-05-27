from django.db import models
from django.contrib.auth.models import User
from customer.models import Address

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2) 
    payment_option = models.CharField(max_length=20, choices=[
        ('Online', 'Online Payment'),
        ('COD', 'Cash on Delivery'),
    ])
    payment_status = models.CharField(max_length=20, choices=[
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
    ],default='Pending')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True) 