from django.db import models

# Create your models here.

from accounts.models import Customer

class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    stock_name = models.CharField(max_length=100)
    disc = models.ImageField()
    price = models.IntegerField()
    
    
class Management(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    pieces = models.IntegerField()
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)