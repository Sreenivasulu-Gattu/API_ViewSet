from django.db import models

# Create your models here.


class Product(models.Model):
    pro_name = models.CharField(max_length = 100)
    pro_price = models.PositiveIntegerField()
    pro_brand = models.CharField(max_length = 100)