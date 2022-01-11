from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    brand = models.CharField(max_length=255)
    desc = models.CharField(max_length=2083,default='shoe')


class Brand(models.Model):
    image_url = models.CharField(max_length=2083)
    brand = models.CharField(max_length=255)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Order(models.Model):

    shoe_id = models.CharField(max_length=10)
    user_id = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    amount = models.FloatField()
    shoe_name = models.CharField(max_length=500, default=1)
    order_date = models.CharField(max_length=50, default=1)
