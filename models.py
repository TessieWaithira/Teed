from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=30)
	desc = models.TextField()
	price = models.FloatField()
	image = models.TextField()
	category_id = models.IntegerField()

	
class Category(models.Model):
	name = models.CharField(max_length=30)
	desc = models.TextField()


class Order(models.Model):
	product_id = models.IntegerField()
	date = models.DateField()
	location = models.TextField()
	user_id = models.IntegerField()
	price = models.FloatField()
	quantity = models.IntegerField()
	batch_id = models.IntegerField()
	status = models.BooleanField()

class Cart(models.Model):
	product_id = models.IntegerField()
	quantity = models.IntegerField()
	price = models.FloatField()

